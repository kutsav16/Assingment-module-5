# Skipping 'banana' in a list using continue

List1 = ['apple', 'banana', 'mango']

for fruit in List1:
    if fruit == 'banana':
        continue   
    print(fruit)
