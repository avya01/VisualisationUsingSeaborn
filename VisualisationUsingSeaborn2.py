import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

file = pd.read_csv("Tips Dataset.csv")

sb.scatterplot(data=file, x=file.total_bill, y=file.tip, hue=file.time, marker="o")
plt.show()