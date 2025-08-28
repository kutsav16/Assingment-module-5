# Demonstrating various string methods

text = "  Hello Python Programming  "

print("Original string:", text)

# Remove leading and trailing spaces
print("strip()        ->", text.strip())

# Convert to uppercase
print("upper()        ->", text.upper())

# Convert to lowercase
print("lower()        ->", text.lower())

# Capitalize first letter
print("capitalize()   ->", text.capitalize())

# Replace a word
print("replace()      ->", text.replace("Python", "Java"))

# Split into words
print("split()        ->", text.split())

# Join words with '-'
words = ["I", "love", "Python"]
print("join()         ->", "-".join(words))

# Check if string starts with 'Hello'
print("startswith()   ->", text.strip().startswith("Hello"))

# Check if string ends with 'ing'
print("endswith()     ->", text.strip().endswith("ing"))

# Find substring position
print("find('Python') ->", text.find("Python"))

# Count occurrences of a character
print("count('o')     ->", text.count("o"))
