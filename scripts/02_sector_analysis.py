# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 11:44:19 2026

@author: shanvan

Sector-level analysis.
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib qt

OUT_DIR = Path("processed/analysis_outputs")
FIG_DIR = Path("figures")
FIG_DIR.mkdir(exist_ok=True)

START_YEAR = 2015
END_YEAR = 2025

sector_year = pd.read_csv(OUT_DIR / "global_sector_year_emissions.csv")

pivot = sector_year.pivot_table(
    index="year",
    columns="sector_clean",
    values="emissions",
    aggfunc="sum",
).fillna(0)

pivot = pivot[pivot.sum().sort_values(ascending=False).index]

plt.figure(figsize=(12, 7))
plt.stackplot(
    pivot.index,
    [pivot[col] for col in pivot.columns],
    labels=pivot.columns,
    alpha=0.85,
)

plt.title("Global GHG Emissions by Sector")
plt.xlabel("Year")
plt.ylabel("Emissions (tonnes CO₂e)")
plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig(FIG_DIR / "global_sector_emissions_stacked.png", dpi=300)
plt.show()

sector_wide = sector_year.pivot_table(
    index=["sector", "sector_clean"],
    columns="year",
    values="emissions",
    aggfunc="sum",
).reset_index()

sector_wide["change_2015_2025"] = sector_wide[END_YEAR] - sector_wide[START_YEAR]
sector_wide["percent_change_2015_2025"] = (
    sector_wide["change_2015_2025"] / sector_wide[START_YEAR]
) * 100

sector_wide.to_csv(OUT_DIR / "global_sector_change_2015_2025.csv", index=False)

plot_data = sector_wide.sort_values("change_2015_2025")

plt.figure(figsize=(9, 6))
plt.barh(plot_data["sector_clean"], plot_data["change_2015_2025"])
plt.axvline(0, color="black", linewidth=1)
plt.xlabel("Change in emissions, 2015–2025 (tonnes CO₂e)")
plt.title("Global Emissions Change by Sector")
plt.grid(axis="x", alpha=0.3)
plt.tight_layout()
plt.savefig(FIG_DIR / "global_sector_change_2015_2025.png", dpi=300)
plt.show()

print(sector_wide.sort_values("change_2015_2025", ascending=False))


