"""
=============================================================
Project : CO2 Time Series Forecasting — Direct Strategy
Author  : Angela
Dataset : Carbon Dioxide Levels in Atmosphere (Mauna Loa)
Goal    : Forecast 3 future CO2 steps using one model per horizon
=============================================================
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def create_direct_data(data, window_size, target_size):
    """Create lag features and multiple target columns for direct forecasting."""
    df = data.copy()
    for i in range(1, window_size):
        df[f'co2_{i}'] = df['co2'].shift(-i)
    for i in range(target_size):
        df[f'target_{i}'] = df['co2'].shift(-(i + window_size))
    return df.dropna()


# ─────────────────────────────────────────
# 1. LOAD DATA
# ─────────────────────────────────────────
if os.path.exists('archive.csv'):
    data = pd.read_csv('archive.csv')
elif os.path.exists('archive (1).csv'):
    data = pd.read_csv('archive (1).csv')
elif os.path.exists('co2.csv'):
    data = pd.read_csv('co2.csv')
else:
    raise FileNotFoundError('Please place archive.csv in this folder!')

data.columns = data.columns.str.strip()
data = data.rename(columns={
    'Decimal Date'         : 'time',
    'Carbon Dioxide (ppm)' : 'co2',
    'Carbon Dioxide'       : 'co2',
})
data = data[['time', 'co2']].dropna()
data['co2'] = pd.to_numeric(data['co2'], errors='coerce')
data = data.dropna()
data['co2'] = data['co2'].interpolate()
print(f'Loaded {len(data)} records')

# ─────────────────────────────────────────
# 2. CREATE FEATURES
# ─────────────────────────────────────────
window_size = 5
num_targets = 3
data_feat   = create_direct_data(data, window_size, num_targets)

target_cols = [f'target_{i}' for i in range(num_targets)]
X = data_feat.drop(['time'] + target_cols, axis=1)
y = data_feat[target_cols]

# ─────────────────────────────────────────
# 3. TRAIN/TEST SPLIT
# ─────────────────────────────────────────
split_idx = int(0.8 * len(data_feat))
X_train, X_test = X[:split_idx], X[split_idx:]
y_train, y_test = y[:split_idx], y[split_idx:]

# ─────────────────────────────────────────
# 4. TRAIN ONE MODEL PER HORIZON
# ─────────────────────────────────────────
models  = [LinearRegression() for _ in range(num_targets)]
results = []

for i, model in enumerate(models):
    model.fit(X_train, y_train[f'target_{i}'])
    y_pred_i = model.predict(X_test)
    results.append({
        'Horizon' : f'Step +{i+1}',
        'MAE'     : round(mean_absolute_error(y_test[f'target_{i}'], y_pred_i), 4),
        'MSE'     : round(mean_squared_error(y_test[f'target_{i}'], y_pred_i), 4),
        'R²'      : round(r2_score(y_test[f'target_{i}'], y_pred_i), 4),
    })

results_df = pd.DataFrame(results)
print('\n📊 Results per Horizon:')
print(results_df.to_string(index=False))

# ─────────────────────────────────────────
# 5. VISUALIZE
# ─────────────────────────────────────────
fig, axes = plt.subplots(3, 1, figsize=(13, 10), sharex=True)

for i, ax in enumerate(axes):
    y_pred_i = models[i].predict(X_test)
    ax.plot(data_feat['time'][split_idx:].values,
            y_test[f'target_{i}'].values,
            label='Actual', color='orange', linewidth=1.5)
    ax.plot(data_feat['time'][split_idx:].values,
            y_pred_i,
            label='Predicted', color='red', linestyle='--', linewidth=1.5)
    ax.set_title(f'Forecast Horizon Step +{i+1}')
    ax.set_ylabel('CO2 (ppm)')
    ax.legend(loc='upper left')
    ax.grid(alpha=0.3)

axes[-1].set_xlabel('Year')
plt.suptitle('CO2 Forecasting — Direct Strategy', fontsize=13)
plt.tight_layout()
plt.savefig('forecast_direct.png', dpi=150)
plt.show()
