import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
df = pd.read_csv("C:\\Alex frfr\\programming\\analysis\\2026_01_A\\tenki(temp).csv")
date = df["date"].tolist()
data = df["Avg"].tolist()
plt.plot(date, data)
plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=12))
plt.xlabel('date')
plt.tick_params(axis='x', labelrotation=67)
plt.ylabel('Average Tempurature [°C]')

# giving a title to my graph
plt.title('Daily Average Tempurature')

# function to show the plot
plt.show()