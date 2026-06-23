# 📊 Dataset Info — Carbon Dioxide Levels in Atmosphere

## 🔗 Download Link

👉 **Kaggle:** https://www.kaggle.com/datasets/ucsandiego/carbon-dioxide

> **How to download:**
> 1. Go to the link above
> 2. Click the **Download** button
> 3. File will be named `archive.csv`
> 4. Place it in the same folder as `main.ipynb`

> ⚠️ **Same dataset as Project 3** — you can copy `archive.csv` from that folder!

---

## 📋 Column Descriptions

| Column | Type | Description |
|--------|------|-------------|
| `Year` | int | Year of measurement |
| `Month` | int | Month of measurement (1–12) |
| `Decimal Date` | float | Year as decimal (e.g. 1958.203) — used as `time` |
| `Carbon Dioxide` | float | CO2 concentration in **ppm** — used as `co2` |
| `Seasonally Adjusted` | float | CO2 with seasonal variation removed |
| `Fit` | float | Curve fit value |

- **Total rows:** ~700+ monthly records
- **Time range:** 1958 — 2017
- **Source:** Scripps Institution of Oceanography, UC San Diego

---

## ⚠️ Note on File Name

Kaggle downloads this dataset as `archive.csv`. The notebook automatically detects:
- ✅ `archive.csv`
- ✅ `archive (1).csv`
- ✅ `co2.csv`
