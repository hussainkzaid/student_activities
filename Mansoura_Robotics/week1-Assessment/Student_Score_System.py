students = []
grades = []
for i in range(3):
    student = input(f"Enter Student {i+1} Name: ")
    students.append(student)
print(students)

print("*"*45)

students_dataset = {}
for student in students:
    grade = int(input(f"Enter The Grade of student {student}: "))
    students_dataset[student] = grade
print(students_dataset)

print("*"*45)

passed_students = {}
for student in students_dataset.keys():
    if students_dataset[student] >= 60:
        student_state = "Passed"
    else:
        student_state = "Failed"

    print(f"Name : {student}\n"
          f"Grade : {students_dataset[student]}\n"
          f"Student State : {student_state}")
    print("*"*20)


    if student_state == "Passed" :
        passed_students[student] = students_dataset[student]

print("*"*45)

print(f"Students Who Passed:\n{passed_students}")

print("*"*45)

unique_grades = set(students_dataset.values())
print(f"All Unique Grades: {unique_grades}")

