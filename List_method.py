work_hours = int(input("Enter your work hours: "))
houry_wage = int(input("Enter your hourly wage: "))


if work_hours <= 40:
    print("Your wage is: ", work_hours * houry_wage)

else:
    print("Your wage is: ", (40 * houry_wage) + ((work_hours - 40) * houry_wage * 1.5))




number_1= int(input("Enter the first number: "))
number_2= int(input("Enter the second number: "))

if number_1 == number_2 or abs(number_1 - number_2) % 5 == 0:
    print("True")

else:

    print("False")



number_1= input("Enter the first number: ")
number_2= input("Enter the second number: ")

if number_1.isnumeric() and number_2.isnumeric():
    print("The sum of the numbers is: ", int(number_1) + int(number_2))

else:
    print("Invalid input")



country = input("Enter the name of the country: ")
area = int(input("Enter the area of the country: "))
earth_area = 510_100_000

percentile = (area / earth_area) * 100

print(f"The area of {country} is {percentile:.2f}% of the Earth's surface.")


weight = int(input("Enter your weight in kg: "))
height = float(input("Enter your height in meter: "))
bmi = weight / height ** 2

print(f"Your BMI is: {bmi:.2f}")

if bmi < 18.5:
    print("Underweight")

elif 18.5 <= bmi < 25:
    print("Normal weight")

elif 25 <= bmi < 30:
    print("Overweight")

else:
    print("Obesity")



given_str = "My phone number is 1234. Please call me!"

output = ""
for i in given_str:
    if i.isnumeric():
        output += i

print(output)

i = 1

while (i < 7):

    if(not(i == 2) and (not(i == 5))):

        print(i)

    i += 1



grade = int(input("Enter your grade: "))
if grade >= 0 or grade <= 100:
    if grade >= 80:
        print("A")

    elif 60 <= grade < 80:
        print("B")

    elif 50 <= grade < 60:
        print("C")

    elif 45 <= grade < 50:
        print("D")

    else:
        print("F")

else:
    print("Invalid grade")



your_name = input("Enter your name: ")

your_name = your_name.lower()
name = []
for char in your_name:
    name.append(char.upper())
print("".join(name))


your_name = input("Enter your name: ")

your_name = your_name.lower()
name_variations = []

if your_name.isalpha():
    for i in range(len(your_name)):
        new_name = your_name[:i] + your_name[i].upper() + your_name[i+1:]
        name_variations.append(new_name)
    print(name_variations)

else:
    print("Invalid input")


your_name = input("Enter your name: ")

if not your_name.isalpha():
    if any(char.isdigit() for char in your_name):
        your_name = ''.join(filter(str.isalpha, your_name))
    else:
        print("Invalid input")
        exit()

your_name = your_name.lower()
name_variations = []
for i in range(len(your_name)):
    new_name = your_name[:i] + your_name[i].upper() + your_name[i+1:]
    name_variations.append(new_name)
print(name_variations)


a = input("Enter the first figure: ")
if a.isdigit():
    if int(a) in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        result = int(a) + int(a * 2) + int(a * 3)

    else:
        print("Invalid input")
else:
    print("Invalid input")

print(result)



number_list = [1,4,9,7,6,12,15,17]
sum = 0
for i in number_list:
    if i % 2:
        sum += i
 
print(sum)


text = "Python is a programming language that lets you work quickly and integrate systems more effectively."
words = text.lower().split()
first_word = words[0]

# Replace first word with asterisks, keep other words
result = " ".join("*" if word == first_word else word for word in words)
print(result)
