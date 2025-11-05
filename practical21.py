import pandas as pd
de={'City': 'Delhi', 'Maxtemp' : 40, 'Mintemp' : 32, 'Rainfall' : 24.1}
be={'City': 'Bengaluru', 'Maxtemp' : 31, 'Mintemp' : 25, 'Rainfall' : 36.2}
ch={'City': 'Chennai', 'Maxtemp' : 35, 'Mintemp' : 27, 'Rainfall' : 40.8}
mu={'City': 'Mumbai', 'Maxtemp' : 29, 'Mintemp' : 21, 'Rainfall' : 35.2}
ko={'City': 'Kolkata', 'Maxtemp' : 39, 'Mintemp' : 23, 'Rainfall' : 41.8}
al={'City': 'Allahabad', 'Maxtemp' : 41, 'Mintemp' : 30, 'Rainfall' : 32.4}
l1=[de,be,ch,mu,ko,al]
df=pd.DataFrame(l1)
print(df)

#Part A
df['Humidity']=[54,65,70,75,71,59]
print(df)

#Part B
print(df.Maxtemp , df.Mintemp)

#Part C
df.to_csv('C:\\Users\\admin\\Desktop\\Weather.csv', index=False)

#Part D
df.rename(columns={'Maxtemp' : 'MxT', 'Mintemp' : 'Mnt'}, inplace=True)
print(df)

#Part E
print(df.tail(5))

#Part F
print(df.count())

#Part G
print(df.T)