# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 11:45:06 2026

@author: shanvan

Country-level analysis.
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib qt

OUT_DIR = Path("processed/analysis_outputs")
FIG_DIR = Path("figures")
FIG_DIR.mkdir(exist_ok=True)

country_summary = pd.read_csv(OUT_DIR / "country_summary_2015_2025.csv")

top_2025 = country_summary.sort_values("emissions_2025", ascending=False).head(20)

plt.figure(figsize=(9, 7))
plt.barh(top_2025["country_name"][::-1], top_2025["emissions_2025"][::-1])
plt.xlabel("Emissions in 2025 (tonnes CO₂e)")
plt.title("Top 20 Emitting Countries in 2025")
plt.grid(axis="x", alpha=0.3)
plt.tight_layout()
plt.savefig(FIG_DIR / "top_20_emitters_2025.png", dpi=300)
plt.show()

largest_increases = country_summary.sort_values(
    "change_2015_2025", ascending=False
).head(20)

plt.figure(figsize=(9, 7))
plt.barh(largest_increases["country_name"][::-1], largest_increases["change_2015_2025"][::-1])
plt.xlabel("Change in emissions, 2015–2025 (tonnes CO₂e)")
plt.title("Largest Emissions Increases by Country")
plt.grid(axis="x", alpha=0.3)
plt.tight_layout()
plt.savefig(FIG_DIR / "largest_country_increases_2015_2025.png", dpi=300)
plt.show()

largest_decreases = country_summary.sort_values(
    "change_2015_2025", ascending=True
).head(20)

plt.figure(figsize=(9, 7))
plt.barh(largest_decreases["country_name"], largest_decreases["change_2015_2025"])
plt.axvline(0, color="black", linewidth=1)
plt.xlabel("Change in emissions, 2015–2025 (tonnes CO₂e)")
plt.title("Largest Emissions Decreases by Country")
plt.grid(axis="x", alpha=0.3)
plt.tight_layout()
plt.savefig(FIG_DIR / "largest_country_decreases_2015_2025.png", dpi=300)
plt.show()

country_summary.to_csv(
    OUT_DIR / "gis_country_emissions_2015_2025.csv",
    index=False,
)

print("Saved GIS-ready country summary.")

