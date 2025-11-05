'''n=int(input("Enter any number: "))
i = 1
j = 1
while i in range (n+1):
    while j in range (i+1):
        print(i*j, end=" ")
        j+=1
    i+=1
    print()
    j=1


# prime
n=int(input("enter a number: "))
for i in range(2,n):
    if n % i== 0:
        print("not prime")
        break

    else:
        print("prime")


# prime numbers in a range

start=int(input("enter start number: "))
end=int(input("enter end number: "))
for i in range(start,end+1):
    for j in range(2,i):
        if i % j == 0:
            print("not a prime number", i)
            break

        else:
            print("prime number", i)


# first 100 prime numbers
count=0
num = 2
while count < 100:
    for i in range(2,num):
        if num % i == 0:
            print("not a prime number")
            break
        else:
            print("prime number")
            count += 1

        num += 1 


# Factorial
n=int(input("enter any number"))
fact = 1
for i in range (1,n+1):
    fact *= i

print("factorial of", n, "is", fact)

# strong number
n=int(input("Enter any Number: "))
orig = n #store orignal
sum=0

while n > 0:
    j = n % 10
    fact = 1
    for i in range(1,j+1):
        fact *= i
    sum += fact
    n //=10

if sum == orig:
    print("Strong Number")

else:
    print("not strong number")


start=int(input("enter start number: "))
end=int(input("enter end number: "))
for i in range(start,end+1):
    for j in range(2,i):
        if i % j == 0:
            print("not a prime number", i)
            break
    else:
        print("prime number", i) 

n=int(input("enter the number: "))
sum = 0
orig = n
while n>0:
    j = n % 10
    fact = 1
    for i in range (1,j+1):
        fact *= i
    sum += fact
    n //= 10
if sum == orig:
    print("s")
else:
    print("ns")


# fibonacci
n=int(input("Enter the number: "))
a,b = 0,1

for i in range(n):
    print(a, end=" ")
    a,b=b,a+b


#sum of digits
n = int(input("enter the number: "))
sum = 0 
orig = n
while n > 0:
    digit = n%10
    sum += digit
    n //= 10

print (sum) '''


# pattern
for i in range(1,6):
    for j in range(1,i+1):
        print(j, end="")
    print()

#binary conversion
n=int(input("enter decimal number: "))
binary=""
while n > 0:
    rem = n % 2
    binary = str(rem) + binary
    n //=2

print(binary)

#palindrome
num = input("Enter number: ")
if num == num[::-1]:
    print(num, "is Palindrome")
else:
    print(num, "is not Palindrome")

