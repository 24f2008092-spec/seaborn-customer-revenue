# Email: 24f2008092@ds.study.iitm.ac.in

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# --- Generate synthetic monthly revenue data ---
np.random.seed(42)
months = pd.date_range(start="2024-01-01", periods=12, freq="M")
revenue = np.linspace(80, 120, 12) + np.random.normal(0, 5, 12)

df = pd.DataFrame({
    "Month": months,
    "Revenue": revenue
})

# --- Seaborn Styling ---
sns.set_style("whitegrid")
sns.set_context("talk")

# --- Create 512x512 Output ---
plt.figure(figsize=(8, 8))  # 8" * 64 dpi = 512 pixels

sns.lineplot(data=df, x="Month", y="Revenue", marker="o", linewidth=3)

plt.title("Monthly Revenue Trend (Synthetic Data)", fontsize=18)
plt.xlabel("Month")
plt.ylabel("Revenue (in $ thousands)")

plt.xticks(rotation=45)

plt.tight_layout()

# --- Save at EXACTLY 512x512 pixels ---
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
