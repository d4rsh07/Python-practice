""" print("Hello World", "I  am Darsh Gaur", sep=" | ", end="\n")
name="darsh"
score=95
print(f"Hi my name is {name} and my score is {score}") 

fruits=[]
n = int(input("Enter the length of list: "))
for i in range(1,n+1):
    x=input("Enter the name of Fruits: ")
    fruits.append(x)
print("your list is:", fruits)


# LOOPS
for i in range (5):
    print ("hello")


x=int(input("Enter the number: "))
for i in range(1,x+1):
    print("i love lesbians")

    """

""" count = 1
while count <= 5:
    print("Butter Chicken")
    count += 1

count = 0
while True:
    print("NoobMaster69")
    count += 1
    if count >= 5:
        break """

'''
# ques 1 
i = 1 
while i <=100:
    print(i)
    i += 1


# ques 2 
i = 100 
while i >= 1:
    print(i)
    i -= 1

# ques 3
n=int(input("Enter any Number: "))
i = 1
while i <= 10:
    print(f"{n} X {i} = ", n * i)
    i += 1

# ques 4
l = [1,4,9,16,25,36,49,64,81,100]
i = 0 
while i <= 9:
    print(l[i])
    i += 1 

# ques 5
l = [1,4,9,16,25,36,49,64,81,100]
i = 0
n=int(input("Enter the number you want to search: "))
while i <= 9:
    if l[i] == n:
        print("your number is at", l.index(n), "index")
        break 
    else:
        print("Finding...")
        i += 1 ''' 

'''
# printing all even number 
i = 1
while i <= 10:
    if i % 2 != 0:
        i += 1
        continue
    print (i)
    i += 1

# ques 1
l=[1,4,9,16,25,36,49,64,81,100]
for i in l:
    print(i)


# ques 2
l=[1,4,9,16,25,36,49,64,81,100]
n=int(input("Enter the number you want to search: "))
j = 0
for i in range (0,n+1) :
    if l[i] == n:
        print(f"number found at {i} index")
        j += 1
'''

n=int(input("Enter a number: "))
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print(sum)


n=int(input("Enter a number: "))
sum = 0
for i in range (1,n+1):
    sum += i 
print(sum) 


n=int(input("Enter a number: "))
fact = 1
for i in range(1,n+1):
    fact *= i
print (fact)


n=int(input("Enter a number: "))
i = 1
fact = 1
while i <= n:
    fact *= i
    i += 1
print (fact)


n=int(input("Enter a number: "))
for i in range(1,n):
    if n % i == 0:
        print("Not a prime number")
        break
else:
    print("number is prime")
    


