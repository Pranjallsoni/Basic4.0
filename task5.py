#TASK5
#1
student = {
    "Shreya": 100,
    "Ishaan":95,
    "Aditi": 80,
    "Veer": 98
}
name = input("Enter student name: ")
if name in student:
    print(f"{name}, scored marks {student[name]}")
else:
    print("Sorry, this name does not exists in record.")

#2
numbers = list(range(1,11))
first_five = numbers[:6]
reversed_five = first_five[::-1]
print(f"Original List {numbers}")
print(f"First Five elements: {first_five}")
print(f"Reversed of first five elements: {reversed_five}")