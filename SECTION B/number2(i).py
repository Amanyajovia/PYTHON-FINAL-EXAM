# NUMBER 2(i)
student_name = input("Enter student name: ")
student_number =input("Enter student number: ")
programming = int(input("Enter programming mark: "))
data_science = int(input("Enter data science mark: "))
computer_applications = int(input("Enter computer application mark: "))

number_of_course_units = 3
total_mark = 90+87+77
average_mark = total_mark/ number_of_course_units
print(f"The average mark is: {average_mark:.3f}")