student_scores = input("Input a list of student score\n").split()

for i in range(0, len(student_scores)):
    student_scores[i] = int(student_scores[i])
print(student_scores)

highest_score = 0
for i in student_scores:
    if i > highest_score:
        highest_score = i
print(f"The highest score in the class is : {highest_score}")