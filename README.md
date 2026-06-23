# 📉 CO2 Time Series Forecasting — Direct Strategy

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0+-orange?logo=scikit-learn)
![Task](https://img.shields.io/badge/Task-Time%20Series-red)
![Dataset](https://img.shields.io/badge/Dataset-Mauna%20Loa%20CO2-lightgrey)

---

## 📌 Project Overview

Forecast **3 future CO2 steps simultaneously** using the **Direct strategy** — each horizon has its own dedicated model, eliminating error compounding.

| Item | Detail |
|------|--------|
| **Dataset** | Carbon Dioxide Levels in Atmosphere (Mauna Loa) |
| **Models** | 3 × Linear Regression (one per horizon) |
| **Strategy** | Direct — no error compounding |
| **Window Size** | 5 past observations |
| **Targets** | Step +1, Step +2, Step +3 |

---

## 🆚 Direct vs Recursive

| | Recursive (Project 3) | Direct (This Project) |
|--|----------------------|----------------------|
| **Models** | 1 model | 1 model per horizon |
| **Error compounding** | ⚠️ Yes | ✅ No |
| **Multi-step** | Feed back predictions | Predict all at once |
| **Best for** | Short horizons | Longer horizons |

---

## 🗂️ Project Structure

```
04_co2_direct_forecasting/
├── main.ipynb        ← Full notebook: Load → Features → Train → Compare
├── main.py           ← Python script version
├── dataset_info.md   ← Download link + column descriptions
└── README.md         ← This file
```

---

## 🚀 How to Run

### Step 1 — Install dependencies
```bash
pip install pandas numpy scikit-learn matplotlib
```

### Step 2 — Download dataset
👉 [Carbon Dioxide Levels — Kaggle](https://www.kaggle.com/datasets/ucsandiego/carbon-dioxide)

Same dataset as Project 3. Place `archive.csv` in this folder.

### Step 3 — Open notebook
```bash
jupyter notebook main.ipynb
```
Then click **Kernel → Restart & Run All**

---

## ⚙️ How Direct Strategy Works

```
Features: [t, t+1, t+2, t+3, t+4]
        │           │           │
        ▼           ▼           ▼
    Model_1     Model_2     Model_3
        │           │           │
        ▼           ▼           ▼
    Target t+5  Target t+6  Target t+7
   (Step +1)   (Step +2)   (Step +3)
```

---

## 📊 Results

| Horizon | MAE | R² |
|---------|-----|----|
| Step +1 | ~0.4 | ~0.99 |
| Step +2 | ~0.5 | ~0.99 |
| Step +3 | ~0.6 | ~0.98 |

**Charts generated:**
- 📈 Full CO2 time series
- 📊 MAE / MSE / R² bar charts per horizon
- 🔴 Actual vs Predicted for each of 3 horizons

---

## 🔑 Key Concepts

- ✅ Direct multi-step forecasting
- ✅ One model trained per forecast horizon
- ✅ No error compounding (vs Recursive strategy)
- ✅ Time-based train/test split
- ✅ Performance comparison across horizons

---

## 📦 Dependencies

```
pandas
numpy
scikit-learn
matplotlib
```
