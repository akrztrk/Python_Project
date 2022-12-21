
student_heights = input("Input a list of student heights\n ").split()
for i in range(0, len(student_heights)):
    student_heights[i] = int(student_heights[i])
print(student_heights)

total_height = 0
for i in student_heights:
    total_height += i
print(total_height)

number_of_students = 0
for i in student_heights:
    number_of_students += 1
print(number_of_students)

avarage_height = round(total_height / number_of_students)
print(avarage_height)