# 🌍 Climate TRACE Greenhouse Gas Emissions Analysis

> **End-to-end analysis of global greenhouse gas emissions using Python, ArcGIS Pro, Power BI, and machine learning.**

This project explores global greenhouse gas (GHG) emissions using the publicly available **Climate TRACE** dataset. The objective was to build a complete data analytics workflow—from raw data processing through statistical analysis, geospatial visualization, machine learning, and interactive dashboard development.

The project was completed as part of my transition from a PhD in Astrophysics to environmental and climate data analytics, demonstrating the application of quantitative research methods to real-world sustainability challenges.

---

## Dashboard Preview

> *Dashboard screenshot coming soon.*

<!-- Replace with an image once complete -->

```markdown
![Power BI Dashboard](dashboard/dashboard_preview.png)
```

---

# Project Objectives

This project investigates several key questions:

* Which sectors contribute most to global greenhouse gas emissions?
* Which countries are the largest emitters?
* Which countries have experienced the greatest emissions changes between 2015 and 2025?
* How do emissions vary geographically?
* Can machine learning identify countries with similar emissions profiles?

---

# Tools & Technologies

| Category         | Tools         |
| ---------------- | ------------- |
| Programming      | Python        |
| Data Analysis    | Pandas, NumPy |
| Visualization    | Matplotlib    |
| Machine Learning | Scikit-learn  |
| GIS              | ArcGIS Pro    |
| Dashboarding     | Power BI      |
| Version Control  | Git & GitHub  |

---

# Workflow

```text
Climate TRACE data
        │
        ▼
Python data cleaning & preprocessing
        │
        ▼
Exploratory Data Analysis
        │
        ├── Country-level analysis
        ├── Sector-level analysis
        ├── Statistical summaries
        └── Machine learning
        │
        ▼
ArcGIS Pro mapping
        │
        ▼
Interactive Power BI dashboard
```

---

# Repository Structure

```text
.
├── dashboard/
│   ├── Climate_TRACE_Dashboard.pbix
│   └── dashboard_preview.png
│
├── figures/
│   ├── emissions_map.png
│   ├── emissions_change_map.png
│   ├── emissions_percent_change_map.png
│   ├── sector_analysis.png
│   └── clustering.png
│
├── powerbi_exports/
│
├── scripts/
│   ├── 01_build_analysis_tables.py
│   ├── 02_sector_analysis.py
│   ├── 03_country_analysis.py
│   ├── 04_emissions_center_of_mass.py
│   ├── 05_ml_clustering.py
│   └── 06_powerbi_exports.py
│
├── README.md
└── requirements.txt
```

---

# Key Analyses

## Country Analysis

* Largest emitting countries
* Absolute emissions changes (2015–2025)
* Percentage emissions changes
* Country rankings
* Interactive Power BI exploration

---

## Sector Analysis

* Global emissions by sector
* Sector contributions through time
* Sector shares
* Sector growth between 2015 and 2025

---

## Geospatial Analysis

Using **ArcGIS Pro**, thematic maps were produced illustrating:

* Global greenhouse gas emissions
* Absolute emissions change
* Percentage emissions change

---

## Machine Learning

An unsupervised machine learning workflow was developed to explore similarities among countries based on their emissions profiles.

Methods include:

* Principal Component Analysis (PCA)
* K-Means clustering
* Feature standardization
* Cluster interpretation

---

# Power BI Dashboard

The Power BI dashboard enables interactive exploration of:

* Global emissions
* Country-level emissions
* Sector contributions
* Emissions trends through time
* Geographic patterns
* Machine learning results

---

# Skills Demonstrated

* Data cleaning and preprocessing
* Exploratory data analysis (EDA)
* Statistical analysis
* Data visualization
* Geospatial analysis (GIS)
* Dashboard development
* Machine learning
* Reproducible Python workflows
* Technical documentation
* Git version control

---

# Data Source

This project uses greenhouse gas emissions data from the **Climate TRACE** initiative.

Climate TRACE is a global coalition that estimates greenhouse gas emissions using satellite observations, remote sensing, and other independent data sources.

https://climatetrace.org/

---

# Future Improvements

Potential extensions include:

* Asset-level emissions analysis
* Time-series forecasting
* Additional machine learning models
* Automated data update pipeline
* Interactive web dashboard deployment

---

# About Me

**Shannon Vanderwoude**

PhD in Astronomy & Astrophysics
University of Toronto

I'm interested in applying quantitative research methods, statistics, machine learning, and geospatial analytics to environmental, climate, healthcare, and public-sector challenges.

Feel free to connect with me on LinkedIn or explore my other repositories.
