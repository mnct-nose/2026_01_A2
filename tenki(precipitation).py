import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
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
plt.figure(figsize=(12, 5))
plt.bar(rain_df["date"], rain_df["precip"])
plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=12))
plt.xlabel("Date")
plt.ylabel("Precipitation [mm]")
plt.title("Daily Precipitation")
plt.tick_params(axis="x", labelrotation=67)
plt.tight_layout()
plt.savefig("tenki(precipitation).png", dpi=300)

plt.show()