import pandas as pd 
d1= {"CompName" : ["Toyota", "Honda", "BMW", "Audi", "Dodge", "Isuzu"], "HorsePower" : [141,80,182,160,68,78], "Price" : [23845,17995,135925,71400,62290,67850], 
     "AvgMileage" : [21,24,16,19,31,25]}
df=pd.DataFrame(d1)


#part 2
print(df.head(2))
print(df.tail(2))

#part 3
df.loc[6]=["Porche",120,89750,27]

#part 4
print(df.loc[6::-1])

#part  5
print(df[df["AvgMileage"]>20])

#part 6 
import matplotlib.pyplot as plt

plt.plot(df["CompName"], df["AvgMileage"], color='r', marker='D', linewidth=0.6, label='AvgMilage')
plt.title("Car comp. vs Avg milage")
plt.xlabel("Car Company")
plt.ylabel("Avg Milage")
plt.legend()
plt.show()