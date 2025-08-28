""" Print this pattern using nested for loop: 
markdown 
Copy code 
* 
** 
*** 
**** 
*****

"""

for i in range(0,6):
    for j in range(0,i):
        print("* ",end="")
    print()