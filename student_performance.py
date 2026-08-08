students = {
    "Anu": [85, 78, 90],
    "Bala": [70, 75, 68],
    "Cathy": [92, 88, 95],
    "Dinesh": [60, 65, 70]
}

print("Student Performance Analysis")
print("----------------------------")

for name, marks in students.items():
    average = sum(marks) / len(marks)
    print(name, "Average:", round(average, 2))
