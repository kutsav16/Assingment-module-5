# Stop the loop once 'banana' is found using break

List1 = ['apple', 'banana', 'mango']

for fruit in List1:
    if fruit == 'banana':
        print("Found banana, stopping the loop.")
        break
    print(fruit)
