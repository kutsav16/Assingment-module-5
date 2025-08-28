# Program: Calculate grades based on percentage

total_marks = float(input("Enter your marks: "))
max_marks = float(input("Enter maximum marks: "))

# Calculate percentage
per = (total_marks / max_marks) * 100

print(f"Percentage: {per:.2f}%")

if per >= 90:
    print("Grade : A")
elif per >= 80 and per < 90:
    print("Grade : B")
elif per >= 70 and per < 80:
    print("Grade : C")
else:
    print("Grade : D")
