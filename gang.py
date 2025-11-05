import matplotlib.pyplot as plt
x=["Rehaan", 'Darsh', 'Shrey', "Mannu", 'Hawk']
y=[6, 6.5, 8.5, 7.5, 7]
plt.bar(x,y, color=["blue",'black','pink',"green","yellow"])
plt.title("Nashedi Rating")
plt.xlabel("Members")
plt.ylabel("Rating")
plt.show()