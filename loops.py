# fruits = ["apples", "peach", "pear"]
# for fruit in fruits:
#   print(fruit)
#   print(fruit + " pie")

# AVERAGE HEIGHT
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
#   print(student_heights)
#   print(len(student_heights))

  #SOLUTION WORKS BUT DOESNT USE LOOPS
# total_height = sum(student_heights)
# number_of_students = len(student_heights)
# average_height = round(total_height / number_of_students)
# print(average_height)

# total_height = 0
# for height in student_heights:
#     total_height += height
# print(total_height)

# number_of_students = 0
# for student in student_heights:
#     number_of_students += 1
# print(number_of_students)

# average_height = round(total_height / number_of_students)
# print(average_height)

# How to output the highest score from  a list of scores
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)

# highest_score = 0
# for score in student_scores:
#     if score > highest_score:
#         highest_score = score
# print(f"The highest score in the clsee is: {highest_score}")

# using for loops with range fuction, generate a range of numbers to loop through

# for number in range(1, 100):
#     print(number) # prints no 1 - 100

# total = 0
# for number in range(1, 101):
#     total += number
# print(total)

# total = 0
# for number in range(2, 101, 2): #change start of range to 2 and step size to 2
#     total += number
# print(number)
# total2 = 0
# for number in range(1, 101):
#     if number % 2 == 0:
#         total2 += number

# print(total2)


# FizzBuzz Job Interview Question

# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)