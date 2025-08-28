# Practical Example 6: Write a Python program to check if a number is prime using if_else.

num=int(input("Enter any number :"))
flag=True
for i in range(2,num):
    if num%i==0:
        flag=False
        break
    

if flag==False:
    print("Your number is not prime.")
else:
    print("Your number is prime.")