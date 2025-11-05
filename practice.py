import pandas as pd
'''#list of dictionaries
l=[{'Name' : 'Darsh', 'Class' : 'XIIA', 'Stream' : 'Sci'},{'Name' : 'Shreyas', 'Class' : 'XIID', 'Stream' : 'Arts'},
   {'Name' : 'Rehaan', 'Class' : 'XIIB', 'Stream' : 'Com'} ]
df=pd.DataFrame(l)
print(df)
#print(df.rename(columns= {'Name':'Naam'}, inplace=True))
df.loc[3]=['Dhruv', 'XIIC', 'Com']
#print(df.sort_values(by=['Naam'], ascending=False, inplace=True))
df.loc[1,"Stream"]="Sci"
df.drop(columns=["Class"], axis=1, inplace=True)
print(df)

#Dictionary of lists
d={'Name' : ['Darsh', 'Shreyas', 'Rehaan'], 'Class' : ["XIIA", 'XIID', 'XIIB'], 'Stream' : ['Sci', 'Arts' , 'Com']}
df1=pd.DataFrame(d)

#list of Series 
s1=pd.Series(['Darsh', 'XIIA', 'Sci'], index=['Name', 'Class', 'Stream'])
s2=pd.Series(['Shreyas','XIID','Arts'], index=['Name', 'Class', 'Stream'])
s3=pd.Series(['Rehaan', 'XIIB', 'Com'], index=['Name', 'Class', 'Stream'])
l1=[s1,s2,s3]
df2=pd.DataFrame(l1)

#Dictionary of Series
s1=pd.Series(['Darsh', 'Shreyas', 'Rehaan'], index=['Stud1', "Stud2", "Stud3"])
s2=pd.Series(['XIIA','XIID','XIIB'],index=['Stud1', "Stud2", "Stud3"])
s3=pd.Series(['Sci', 'Arts', 'Com'], index=['Stud1', "Stud2", "Stud3"])
d2={'Name' : s1,'Class' : s2, 'Stream' : s3}
df3=pd.DataFrame(d2)'''

#Dictionary of Dictionaries
d1={'0' : 'Riri', '1':'Tom', '2': 'Lala'}
d2={'0': 'Rara',  '1' : 'Tommy', '2': 'Lolo'}
d3={'0':'Ruru','1' : 'Tammy', '2' : 'Lili' }

d4={'Name' : d1, 'Father' :  d2, 'Mother' : d3}
df4=pd.DataFrame(d4)
print(df4)
