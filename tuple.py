students_info = [("Nabil", 33, 58), ("Pratik", 33, 87), ("Masum", 33, 29), ("Tacin", 33, 88)]
final_students = sorted(students_info, key=lambda x: x[2])
print(final_students)