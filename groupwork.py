def capture_student_details():
    student = {}
    student['Name'] = input("Enter student's Name: ")
    student['Age'] = int(input("Enter student's Age: "))
    student['Gender'] = input("Enter student's Gender: ")
    student['Program'] = input("Enter student's Program: ")
    student['Year_of_study'] = int(input("Enter student's Year of study: "))
    student['Faculty'] = input("Enter student's Faculty: ")
    student['Date_of_Birth'] = input("Enter student's Date of Birth (YYYY-MM-DD): ")
    student['test1'] = float(input("Enter student's Test 1 marks: "))
    student['test2'] = float(input("Enter student's Test 2 marks: "))
    student['final_exam'] = float(input("Enter student's Final Exam marks: "))
    return student

def calculate_average_marks(student):
    total_marks = student['test1'] + student['test2'] + student['final_exam']
    average_marks = total_marks / 3
    return average_marks

def capture_test_marks():
    while True:
        try:
            test1 = float(input("Enter student's Test 1 marks: "))
            test2 = float(input("Enter student's Test 2 marks: "))
        except ValueError:
            print("Please enter valid numbers.")
            







