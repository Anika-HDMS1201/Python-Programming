# =====================================================================
# 1. IMPORTS — Check VS Code here!
# If any line below has a yellow squiggly underline, that package is 
# either not installed or VS Code is pointing to the wrong Python.
# =====================================================================
import numpy as np
import pandas as pd
import openpyxl
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from sklearn.linear_model import LinearRegression
from xgboost import XGBRegressor
from lightgbm import LGBMRegressor
import mysql.connector
import ipykernel

print("✅ Step 1: All 13 MBA Data Analytics libraries imported successfully!\n")

# =====================================================================
# 2. NUMPY & PANDAS — Create a simple business dataset
# =====================================================================
np.random.seed(42)
ad_spend = np.linspace(10, 100, 30)
sales = 25 + (2.5 * ad_spend) + np.random.normal(0, 10, 30)

df = pd.DataFrame({
    "Ad_Spend": ad_spend,
    "Sales": sales
})
print(f"✅ Step 2 (NumPy & Pandas): Created dataset with {len(df)} rows.")

# =====================================================================
# 3. OPENPYXL — Save to Excel and read it back
# =====================================================================
excel_file = "mba_test_data.xlsx"
df.to_excel(excel_file, index=False, engine="openpyxl")
df_excel = pd.read_excel(excel_file, engine="openpyxl")
print(f"✅ Step 3 (OpenPyXL): Saved and loaded '{excel_file}' ({df_excel.shape[0]} rows) | v{openpyxl.__version__}")

# =====================================================================
# 4. SCIPY — Run a statistical correlation test
# =====================================================================
corr, p_val = stats.pearsonr(df["Ad_Spend"], df["Sales"])
print(f"✅ Step 4 (SciPy): Pearson Correlation = {corr:.3f} (p-value = {p_val:.4e})")

# =====================================================================
# 5. STATSMODELS — Run an Econometric OLS Regression
# =====================================================================
X_sm = sm.add_constant(df["Ad_Spend"])
ols_model = sm.OLS(df["Sales"], X_sm).fit()
print(f"✅ Step 5 (Statsmodels): OLS R-squared = {ols_model.rsquared:.3f}")

# =====================================================================
# 6. SCIKIT-LEARN, XGBOOST & LIGHTGBM — Predict Sales for Ad Spend = 60
# =====================================================================
X = df[["Ad_Spend"]]
y = df["Sales"]
new_data = pd.DataFrame({"Ad_Spend": [60.0]})

# Scikit-Learn
sk_model = LinearRegression().fit(X, y)
sk_pred = sk_model.predict(new_data)[0]

# XGBoost
xgb_model = XGBRegressor(n_estimators=10, verbosity=0).fit(X, y)
xgb_pred = xgb_model.predict(new_data)[0]

# LightGBM
lgb_model = LGBMRegressor(n_estimators=10, min_child_samples=2, verbose=-1).fit(X, y)
lgb_pred = lgb_model.predict(new_data)[0]

print(f"✅ Step 6 (Machine Learning Predictions for Ad Spend = 60):")
print(f"   • Scikit-Learn : {sk_pred:.2f}")
print(f"   • XGBoost      : {xgb_pred:.2f}")
print(f"   • LightGBM     : {lgb_pred:.2f}")

# =====================================================================
# 7. MYSQL & IPYKERNEL — Verify driver & notebook kernel readiness
# =====================================================================
print(f"✅ Step 7 (Database & Kernel):")
print(f"   • MySQL Connector Ready : v{mysql.connector.__version__}")
print(f"   • IPyKernel Ready       : v{ipykernel.__version__}")

# =====================================================================
# 8. PLOTLY — Generate an interactive HTML chart
# =====================================================================
plotly_fig = px.scatter(df, x="Ad_Spend", y="Sales", title="Plotly: Ad Spend vs Sales")
plotly_fig.write_html("mba_plotly_test.html")
print("✅ Step 8 (Plotly): Saved interactive chart to 'mba_plotly_test.html'.")

# =====================================================================
# 9. MATPLOTLIB & SEABORN — Plot regression line and display window
# =====================================================================
plt.figure(figsize=(7, 4))
sns.regplot(data=df, x="Ad_Spend", y="Sales", color="teal")
plt.title("Matplotlib + Seaborn: Ad Spend vs Sales Trend", fontweight="bold")
plt.tight_layout()
print("✅ Step 9 (Matplotlib & Seaborn): Opening chart window now...")
plt.show()