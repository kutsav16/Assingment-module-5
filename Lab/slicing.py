# Demonstrating string slicing in Python

text = "utsavkathiriya"
print("Original string:", text)

# Slice from index 0 to 5
print("text[0:5]  ->", text[0:5])    

# Slice from index 3 to end
print("text[3:]   ->", text[3:])      

# Slice from start to index 6
print("text[:6]   ->", text[:6])      

# Slice with step 
print("text[::2]  ->", text[::2])     

# Slice with negative index
print("text[-5:]  ->", text[-5:])     

# Reverse the string
print("text[::-1] ->", text[::-1])    
