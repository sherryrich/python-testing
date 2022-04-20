# print("hello")
# input() will get user to input in console
# Then print() will print the word "hello" and the user input
# print("Hello " + input("what is your name?"))# stops running until user enters input
# print("Python Print Function")
# print("The function is declared like this:")
# print("print('what to print')")

# print("Day 1 - String Manipulation")
# print("String Concatenation is done with the "+" sign.")
# print('e.g. print("Hello " + "world")')
# print("New lines can be created with a backslash and n.")
# prints the number of characters in name
# print( len( input("What is your name?") ) ) 
# variables
# name = input("what is your name?")
# print(name)

# name = "jack"
# print(name)

# name = "Peter"
# print(name)

# name = input("what is your name?")
# lenght = len(name)
# print(lenght)

# variable naming
# user_name 1 single unit, if seperated use underscore. no number at the start and dont use reserved key words like input or print
 # name error will show if typo in the variable

#  #1. Create a greeting for your program.
# print("welcome to the band name generator")
# #2. Ask the user for the city that they grew up in.
# city = input("what city did you grow up in?\n")
# #3. Ask the user for the name of a pet.
# pet = input("what is the name of you pet?\n")
# #4. Combine the name of their city and pet and show them their band name.
# print("Your bank name coulb be " + city + " " + pet)
# #5. Make sure the input cursor shows on a new line, see the example at:


#day 3 Rollercoaster if statement
# print("welcome to the rollercoaster")
# height = int(input("what is your height in cm?"))

# if height >= 120:
#     print("you can ride the rollercoaster")
# else:
#     print("Sorry, you have to grow tallker before you can ride")

#day 3 Odd /Even number calc
# number = int(input("Which number do you want to check? "))
# if number % 2 == 0:
#     print("this is an even number")
# else:
#     print("this is an odd number")


# Nested if statements

# print("welcome to the rollercoaster")
# height = int(input("what is your height in cm?"))

# if height >= 120:
#     print("you can ride the rollercoaster")
#     age = int(input("what is your age?"))
#     if age <= 12:
#         print("please pay €5")
#     elif age <= 18:
#         print("please pay €7")
#     else:
#         print("please pay €12")

#BMI Calc
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi = round(weight / height ** 2)
if bmi < 18.5:
    print(f"Your bmi is {bmi}, you are underwight")
elif bmi < 25:
    print(f"Your bmi is {bmi}, you a have a normal weight")
elif bmi < 30:
    print(f"Your bmi is {bmi}, you are overwight")
elif bmi < 35:
    print(f"Your bmi is {bmi}, you are obese")