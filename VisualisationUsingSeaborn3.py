import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

file = pd.read_csv("Tips Dataset.csv")

sb.pairplot(file, hue="gender")
plt.show()