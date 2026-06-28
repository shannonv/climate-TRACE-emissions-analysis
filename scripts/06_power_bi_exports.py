# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 11:47:00 2026

@author: shanvan

Power BI exports.
"""

from pathlib import Path
import pandas as pd

OUT_DIR = Path("processed/analysis_outputs")
PBI_DIR = Path("powerbi_exports")
PBI_DIR.mkdir(exist_ok=True)

# -----------------------------
# Core exports
# -----------------------------

core_files = [
    "country_year_emissions.csv",
    "country_sector_year_emissions.csv",
    "country_summary_2015_2025.csv",
    "global_sector_year_emissions.csv",
    "global_sector_change_2015_2025.csv",
]

for file in core_files:
    df = pd.read_csv(OUT_DIR / file)
    df.to_csv(PBI_DIR / file, index=False)
    print(f"Exported: {file}")

# -----------------------------
# ML cluster exports
# -----------------------------

cluster_file = OUT_DIR / "country_emissions_clusters.csv"

if cluster_file.exists():
    clusters = pd.read_csv(cluster_file)

    # Full country-level cluster membership
    clusters.to_csv(
        PBI_DIR / "country_emissions_clusters.csv",
        index=False
    )

    # Cluster summary table
    cluster_summary = (
        clusters.groupby("cluster", as_index=False)
        .agg(
            country_count=("iso3_country", "count"),
            mean_emissions_2025=("emissions_2025", "mean"),
            median_emissions_2025=("emissions_2025", "median"),
            mean_change_2015_2025=("change_2015_2025", "mean"),
            median_change_2015_2025=("change_2015_2025", "median"),
            mean_percent_change_2015_2025=("percent_change_2015_2025", "mean"),
            median_percent_change_2015_2025=("percent_change_2015_2025", "median"),
        )
    )

    cluster_summary.to_csv(
        PBI_DIR / "cluster_summary.csv",
        index=False
    )

    # Cluster sector profiles
    sector_cols = [
        col for col in clusters.columns
        if col not in [
            "iso3_country",
            "country_name",
            "emissions_2025",
            "change_2015_2025",
            "percent_change_2015_2025",
            "cluster",
            "PC1",
            "PC2",
        ]
    ]

    cluster_sector_profile = (
        clusters.groupby("cluster")[sector_cols]
        .mean()
        .reset_index()
    )

    cluster_sector_profile.to_csv(
        PBI_DIR / "cluster_sector_profiles.csv",
        index=False
    )

    # PCA coordinates for scatter plot in Power BI
    pca_cols = [
        "iso3_country",
        "country_name",
        "cluster",
        "PC1",
        "PC2",
        "emissions_2025",
        "change_2015_2025",
        "percent_change_2015_2025",
    ]

    existing_pca_cols = [col for col in pca_cols if col in clusters.columns]

    clusters[existing_pca_cols].to_csv(
        PBI_DIR / "cluster_pca_points.csv",
        index=False
    )

    print("Exported ML cluster files.")

else:
    print("No cluster file found. Run 05_ml_clustering.py first.")

print("Power BI export files saved to:", PBI_DIR)
