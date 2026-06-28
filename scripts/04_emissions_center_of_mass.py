# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 11:45:47 2026

@author: shanvan

Emissions center of mass.
"""

from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib qt

OUT_DIR = Path("processed/analysis_outputs")
FIG_DIR = Path("figures")
FIG_DIR.mkdir(exist_ok=True)

# You need to create this from ArcGIS or another source:
# columns required: iso3_country, centroid_lat, centroid_lon
CENTROID_FILE = OUT_DIR / "country_centroids_clean.csv"

country_year = pd.read_csv(OUT_DIR / "country_year_emissions.csv")
centroids = pd.read_csv(CENTROID_FILE)

data = country_year.merge(centroids, on="iso3_country", how="inner")

def weighted_center(group):
    return pd.Series({
        "weighted_lat": np.average(group["centroid_lat"], weights=group["emissions"]),
        "weighted_lon": np.average(group["centroid_lon"], weights=group["emissions"]),
        "total_emissions": group["emissions"].sum(),
    })

center = (
    data.groupby("year")
    .apply(weighted_center)
    .reset_index()
)

center.to_csv(OUT_DIR / "emissions_center_of_mass_2015_2025.csv", index=False)

plt.figure(figsize=(8, 6))
plt.plot(center["weighted_lon"], center["weighted_lat"], marker="o", linewidth=2)

for _, row in center.iterrows():
    plt.text(row["weighted_lon"], row["weighted_lat"], str(int(row["year"])), fontsize=8)

plt.xlabel("Weighted longitude")
plt.ylabel("Weighted latitude")
plt.title("Global Centre of GHG Emissions, 2015–2025")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig(FIG_DIR / "global_emissions_center_of_mass.png", dpi=300)
plt.show()

print(center)

