#  Write a Python program to find a specific string in the list using a simple for loop and if condition. 

List1 = ['apple', 'banana', 'mango'] 

search=input("Enter your find string :")
flag=0
for i in List1:
    if i==search:
        flag=1
        break
        
if flag==1:
    print(f"{search} value in a list")
     
else:
    print(f"{search} value in not over list")
    