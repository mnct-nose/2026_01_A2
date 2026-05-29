import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
df = pd.read_csv("tenki(temp).csv")
while(True):
  try:
    item = str(input("Choose item (Avg / Max / Min)\n"))
    date = df["date"].tolist()
    data = df[item].tolist()
  except KeyError:
    print("please try again")
  else:
    break
px = 1/plt.rcParams['figure.dpi']  # pixel in inches
plt.figure(figsize=(1200*px, 800*px))
plt.plot(date, data)
plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=12))
plt.xlabel('date')
plt.tick_params(axis='x', labelrotation=67)
plt.ylabel('Average Tempurature [°C]')
dict = {
  "Avg": "Average",
  "Max": "Maximum",
  "Min": "Minimum"
}
title = "Daily "+dict[item]+" Tempurature"
# giving a title to my graph
plt.title(title)
name = "tenki(temp)_"+item+".png"
# function to show the plot
plt.savefig(name)
plt.show()
