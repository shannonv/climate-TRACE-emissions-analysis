# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 11:41:02 2026

@author: shanvan

Build analysis tables.
"""

from pathlib import Path
import pandas as pd
import numpy as np
%matplotlib qt

try:
    import pycountry
except ImportError:
    pycountry = None

DATA_DIR = Path("processed")
OUT_DIR = DATA_DIR / "analysis_outputs"
OUT_DIR.mkdir(parents=True, exist_ok=True)

START_YEAR = 2015
END_YEAR = 2025
GAS = "co2e_100yr"
EXCLUDE_FORESTRY = True


def iso3_to_name(code):
    if pycountry is None:
        return code
    country = pycountry.countries.get(alpha_3=code)
    return country.name if country else code


def clean_sector_name(sector):
    return sector.replace("-", " ").replace("and", "&").title()


df = pd.read_csv(DATA_DIR / "sector_level_summary.csv")

df = df[
    (df["gas"] == GAS) &
    (df["year"].between(START_YEAR, END_YEAR))
].copy()

if EXCLUDE_FORESTRY:
    df = df[df["sector"] != "forestry-and-land-use"].copy()

df["country_name"] = df["iso3_country"].apply(iso3_to_name)
df["sector_clean"] = df["sector"].apply(clean_sector_name)

df = df.rename(columns={"sector_emissions_quantity": "emissions"})

master = df[
    [
        "iso3_country",
        "country_name",
        "year",
        "sector",
        "sector_clean",
        "gas",
        "emissions",
    ]
].copy()

master.to_csv(OUT_DIR / "master_trace_analysis.csv", index=False)

country_year = (
    master.groupby(["iso3_country", "country_name", "year"], as_index=False)["emissions"]
    .sum()
)

country_year.to_csv(OUT_DIR / "country_year_emissions.csv", index=False)

country_sector_year = (
    master.groupby(
        ["iso3_country", "country_name", "year", "sector", "sector_clean"],
        as_index=False,
    )["emissions"]
    .sum()
)

country_sector_year.to_csv(OUT_DIR / "country_sector_year_emissions.csv", index=False)

sector_year = (
    master.groupby(["year", "sector", "sector_clean"], as_index=False)["emissions"]
    .sum()
)

sector_year.to_csv(OUT_DIR / "global_sector_year_emissions.csv", index=False)

wide = country_year.pivot_table(
    index=["iso3_country", "country_name"],
    columns="year",
    values="emissions",
    aggfunc="sum",
).reset_index()

wide["change_2015_2025"] = wide[END_YEAR] - wide[START_YEAR]
wide["percent_change_2015_2025"] = (
    wide["change_2015_2025"] / wide[START_YEAR]
) * 100
wide["percent_change_2015_2025"] = wide["percent_change_2015_2025"].replace(
    [np.inf, -np.inf], np.nan
)

wide = wide.rename(columns={
    START_YEAR: "emissions_2015",
    END_YEAR: "emissions_2025",
})

wide.to_csv(OUT_DIR / "country_summary_2015_2025.csv", index=False)

print("Done. Analysis tables saved to:", OUT_DIR)



