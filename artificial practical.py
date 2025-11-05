import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r"C:\Users\admin\Downloads\Rainfall.csv")
x=df["Months"]
y=df["Rainfall(cm)"]
plt.figure(figsize=(6,4))
plt.plot(x,y, marker="o", markersize=8, markeredgecolor='red', markerfacecolor="yellow")
plt.xticks(rotation=45)
plt.xlabel('Months', fontname="Arial", color="b", fontsize=12)
plt.ylabel('Rainfall(cm)', fontname="Arial", color="b", fontsize=12)
plt.title("Rainfall data of Tamil Nadu", fontname="Arial", color="m", fontsize=16)
plt.show()