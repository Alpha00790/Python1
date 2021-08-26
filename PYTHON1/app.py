import math
print("Hello World!")
print("*"*10)
2+5
x = 1
students_count = 1000
rating = 4.99
is_published = True
course_name = 'Python programming!'
print(students_count)
print(rating)
print(is_published)
print(course_name)
print(len(course_name))
print(course_name[-1])
print(course_name[0])
print(course_name[0:5])
print(course_name[0:])
print(course_name[:6])
print("Shaikat \"Barua")
print('Shaikat\nBarua')
print('shaikat\\\nBarua')
firstName = 'Shaikat'
lastName = 'Barua'
fullName = firstName + " " + lastName
print(fullName)
newFullName = f"{firstName} \n{lastName}"
print(newFullName)
practice = f"{len(firstName)} {lastName[0:3]}"
print(practice)

course = 'python ProgramMinG'
print(course.upper())
print(course.lower())
print(course.title())
print(course.find("Pro"))
print(course.replace('python', 'javascript'))
print('py' in course)
print('pro' in course)

a = int(input())
b = int(input())
print(a+b)
print(10+3)
print(10-3)
print(10*3)
print(10/3)
print(10//3)
print(10 % 3)
print(2**3)
x = 10
x += 3
print(x)
print(math.ceil(2.2))
print(abs(-2.5))
print(round(2.6))

x = int(input('X: '))
y = x+1
print(f"X:{x} & Y:{y}")

temperature = 20

if temperature > 30:
    print("It\'s hot weather")
    print("Drink water")
elif temperature > 20:
    print("It\'s okay!")
else:
    print("you\'re going to die!")
print('Bye!')
age = 18
age = 17
message = "Eligible" if age >= 18 else "not Eligible"
print(message)

high_income = True
good_credit = False

print("Eligible for loan!") if high_income and good_credit else print(
    "Not eligible! For loan.")

is_student = True
if not is_student:
    print("Eligible")
else:
    print("not Eligible to be Student")

high_income = True
good_credit = True
student = False

if(high_income or good_credit) and not student:
    print("Accepted")
else:
    print("Rejected")

if __name__ == '__main__':
    n = int(input().strip())
if(n%2 !=0 and n>5 and n<20 ):
    print("Weired")
elif(n%2!=0):
    print("Weired")
else:
    print("Not Weired")

high_income = False
good_credit = True
student = True
student = False
high_income=True

if high_income and good_credit and not student:
    print("Come in!")
if high_income or good_credit or not student:
    print("Come in!")
print("Don't Come!")
age = 22
if age >= 18 and age < 69:
    print("Ignored")

if 18 <= age < 69:
    print("Ignored!")

for number in range(5):
    print("Step Bro!", number)


for number in range(3):
    print('Attempt',number+1)

for number in range(1, 10):
    print('Attempt', number+1)

for number in range(1, 10, 2):
    print('Attempt', number, number*".")


successful = True

for number in range(5):
    print('Attempt')
    if successful:
        print('Successfull')
        break


successful = False

for number in range(5):
    print('Achived')
    if successful:
        print('Successful')
        break
else:
    print('Tried 3 times and broke')

for x in range(1, 5):
    for y in range(1, 3):
        print(f"({x},{y}={x*y})")

for x in 'python':
    print(x)

for x in ([1, 2, 3, 4, 5]):
    print(x)

command = " "
while command != 'quit':
    command = input("++:")
    print("Echo",command)

while command != 'quit' and command != 'QUIT':
    command = input("++:")
    print("Echo",command)

while command.lower() != 'quit':
    command = input("++:")
    print("-->",command)

while True:
    command = input("++:")
    print("-->",command)
    if(command.lower()=='quit'):
        break
