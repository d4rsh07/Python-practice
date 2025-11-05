# line chart
import matplotlib.pyplot as plt
ip=[77,69,65,73,53,59]
acc=[89,26,17,36,92,68]
eco=[83,95,78,74,63,34]
name=['Darsh','Rehaan','Shreyas','Mankirat','Dhruv','Akaash']
plt.plot(name,ip, label='IP', color='k', marker='o')
plt.plot(name,acc, label='ACC', color= 'g', linestyle="dashdot")
plt.plot(name,eco, label='ECO', color='pink', linewidth=3)
plt.xlabel('Names')
plt.ylabel('Marks')
plt.grid(True)
plt.legend()
plt.title('Data of class XII')
plt.show()

#Bar Graph
import matplotlib.pyplot as plt
marks=[86,65,50,100]
subject=["Eng","Acc","Eco","Ip"]
plt.bar(subject,marks, color=["green",'black','red',"pink"])
plt.title("Annual Marks")
plt.show()

#CSV 
import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv(r"C:\Usersadmin\Desktop\chuchu.csv")
df.plot(kind="bar", x="days", align="center")
plt.show()

