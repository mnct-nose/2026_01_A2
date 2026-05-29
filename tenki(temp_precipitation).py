import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
temp_df = pd.read_csv(
    "tenki(temp).csv"
)
temp_df["date"] = pd.to_datetime(temp_df["date"])
temp_df["Avg"] = pd.to_numeric(temp_df["Avg"], errors="coerce")
rain_df = pd.read_csv(
    "tenki(precipitation).csv",
    encoding="cp932",
    skiprows=5,
    header=None,
    names=["year", "month", "day", "precip", "no_event", "quality", "homogeneity"]
)
rain_df["date"] = pd.to_datetime(
    rain_df[["year", "month", "day"]]
)
rain_df["precip"] = pd.to_numeric(rain_df["precip"], errors="coerce")
df = pd.merge(
    temp_df,
    rain_df[["date", "precip"]],
    on="date",
    how="inner"
)
fig, ax1 = plt.subplots(figsize=(12, 5))
ax1.plot(df["date"], df["Avg"], label="Average Temperature")
ax1.set_xlabel("Date")
ax1.set_ylabel("Average Temperature [°C]")
ax1.tick_params(axis="x", labelrotation=67)
ax1.xaxis.set_major_locator(MaxNLocator(nbins=12))
ax2 = ax1.twinx()
ax2.bar(df["date"], df["precip"], alpha=0.3, label="Precipitation")
ax2.set_ylabel("Precipitation [mm]")
plt.title("Daily Average Temperature and Precipitation")
fig.tight_layout()
plt.savefig("tenki(temp_precipitation).png", dpi=300)

plt.show()