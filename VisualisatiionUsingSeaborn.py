import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

file = pd.read_csv("Tips Dataset.csv")

plt.title("Total bill feature")
plt.xlabel("Bill")
plt.ylabel("Number")
sb.histplot(file.total_bill, kde=True)
plt.show()