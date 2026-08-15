import pandas as pd

students_dataset = pd.DataFrame([{'Name': 'Hussain Kamel','Age': 20,'Grade': 97},
                                 {'Name': 'Mohamed Zaid','Age': 21,'Grade': 95},
                                 {'Name': 'Ahmed Nader','Age': 23,'Grade': 85}
                                ])

def add_student(df):
    name = input('Enter The Name: ')
    age =  int(input('Enter The Age: '))
    grade = int(input('Enter The Grade: '))

    new_student = pd.DataFrame([{'Name': name,'Age': age,'Grade': grade}])

    if (df['Name'] == name).any():
        print('Student Is Already Existed')
        print('*********************************************')
        return df

    print("Student updated successfully.")
    print('*********************************************')
    return pd.concat([new_student,df], ignore_index=True)


def update_student(df):

    name = input('Enter The Student Name: ')

    if (df['Name'].str.strip().str.lower() == name.strip().lower()).any():
        new_grade = int(input('Enter The New Grade: '))
        df.loc[df['Name'].str.strip().str.lower() == name.strip().lower(), 'Grade'] = new_grade
        print("Student updated successfully.")
        print('*********************************************')
    else:
        print("Student not found.")
        print('*********************************************')

    return df

def search_student(df):
    name = input('Enter The Student Name: ')

    if (df['Name'].str.strip().str.lower() == name.strip().lower()).any():
        print(df.loc[df['Name'].str.strip().str.lower() == name.strip().lower()])
        print('*********************************************')
    else:
        print("Student not found.")
        print('*********************************************')

def delete_student(df):
    name = input('Enter The Name of Student You Want to Delete: ')

    if (df['Name'].str.strip().str.lower() == name.strip().lower()).any():
        df = df.drop(df.loc[df['Name'].str.strip().str.lower() == name.strip().lower()].index)
        print("Student Deleted successfully.")
        print('*********************************************')
    else:
        print("Student not found.")
        print('*********************************************')

    return df

def show_all_students(df):
    if df.shape[0] > 0 :
        print(df)
        print('*********************************************')
    else :
        print("There Is No Students To Show.")
        print('*********************************************')


while True:
    print("""1. Add Student\n2. Search Student\n3. Update Student Grade\n4. Delete Student\n5. Show All Students\n6. Exit""")

    try:
        choice = int(input("Enter Your Choice: "))
        print('*********************************************')
    except :
        print("Invalid Choice, Enter a Number Between 1 and 6")
        print('*********************************************')
        continue


    if choice == 1:
        students_dataset = add_student(students_dataset)

    elif choice == 2:
        search_student(students_dataset)

    elif choice == 3:
        students_dataset = update_student(students_dataset)

    elif choice == 4:
        students_dataset = delete_student(students_dataset)

    elif choice == 5:
        show_all_students(students_dataset)

    elif choice == 6:
        break

    else :
        print("Invalid Choice, Enter a Number Between 1 and 6")
        print('*********************************************')
