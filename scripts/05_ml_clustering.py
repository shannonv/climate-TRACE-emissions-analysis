# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 11:46:23 2026

@author: shanvan

ML clustering analysis.
"""

from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib qt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

OUT_DIR = Path("processed/analysis_outputs")
FIG_DIR = Path("figures")
FIG_DIR.mkdir(exist_ok=True)

END_YEAR = 2025
N_CLUSTERS = 5

country_sector_year = pd.read_csv(OUT_DIR / "country_sector_year_emissions.csv")
country_summary = pd.read_csv(OUT_DIR / "country_summary_2015_2025.csv")

country_sector_2025 = country_sector_year[
    country_sector_year["year"] == END_YEAR
].copy()

sector_matrix = country_sector_2025.pivot_table(
    index=["iso3_country", "country_name"],
    columns="sector_clean",
    values="emissions",
    aggfunc="sum",
).fillna(0)

sector_shares = sector_matrix.div(sector_matrix.sum(axis=1), axis=0).fillna(0)

features = sector_shares.reset_index().merge(
    country_summary[
        [
            "iso3_country",
            "country_name",
            "emissions_2025",
            "change_2015_2025",
            "percent_change_2015_2025",
        ]
    ],
    on=["iso3_country", "country_name"],
    how="left",
)

features = features.replace([np.inf, -np.inf], np.nan).dropna()
MIN_EMISSIONS = 1e6  # 1 Mt CO₂e

features = features[
    features["emissions_2025"] >= MIN_EMISSIONS
].copy()

feature_cols = [
    col for col in features.columns
    if col not in ["iso3_country", "country_name"]
]

X = features[feature_cols].copy()

X["emissions_2025"] = np.log10(X["emissions_2025"] + 1)
X["change_2015_2025"] = np.sign(X["change_2015_2025"]) * np.log10(
    np.abs(X["change_2015_2025"]) + 1
)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

kmeans = KMeans(n_clusters=N_CLUSTERS, random_state=42, n_init=20)
features["cluster"] = kmeans.fit_predict(X_scaled)

pca = PCA(n_components=2, random_state=42)
coords = pca.fit_transform(X_scaled)

features["PC1"] = coords[:, 0]
features["PC2"] = coords[:, 1]

features.to_csv(OUT_DIR / "country_emissions_clusters.csv", index=False)

plt.figure(figsize=(9, 7))

for cluster, group in features.groupby("cluster"):
    plt.scatter(group["PC1"], group["PC2"], label=f"Cluster {cluster}", alpha=0.75)

plt.xlabel(f"PC1 ({pca.explained_variance_ratio_[0] * 100:.1f}% variance)")
plt.ylabel(f"PC2 ({pca.explained_variance_ratio_[1] * 100:.1f}% variance)")
plt.title("Country Clusters by Emissions Profile")
plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig(FIG_DIR / "country_emissions_clusters_pca.png", dpi=300)
plt.show()

print(features[["iso3_country", "country_name", "cluster"]].sort_values("cluster"))


features.sort_values("cluster").to_csv('cluster_members.csv')
