'''#Histogram
import matplotlib.pyplot as plt
marks=[40,60,55,20,35,70,60,89,20,33]
plt.hist(marks,bins=[0,33,45,60,100], rwidth=0.9,cumulative=True,histtype="bar",align="mid", orientation="horizontal" )
plt.show()

#Histogram2
import matplotlib.pyplot as plt
b=[10,20,11,21,9]
g=[11,23,10,9,6]
plt.hist([b,g],bins=[0,10,20,30],rwidth=0.9,color=['cyan','pink'], label=["Boys", "Girls"])
plt.xlabel("range")
plt.ylabel("ratios")
plt.legend()
plt.show()'''

