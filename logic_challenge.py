# number = int(input("Please enter a number:"))

# if number == 5:
#     print(f"{number} is equal to 5")
# else:
#     print(f"{number} is not equal to 5")


# Challenge
# if the number is divisible by 3 = say "Fizz"
# if the number is divisible by 5 = say "Buzz"
# if the number is divisible by 3 and 5 = say "FizzBuzz"
# Otherwise say the original number

# num = 1

# if num % 3 == 0 and num % 5 == 0:
#     print("FizzBuzz")
# elif num % 3 == 0:
#     print("Fizz")
# elif num % 5 == 0:
#     print("Buzz")
# else:
#     print(num)

#Multiple Conditions (If/Elif/Else)
# number = int(input("Please enter a number:"))

# if number > 5:
#     print(f"{number} is greater than 5")
# elif number < 5:
#     print(f"{number} is less than 5")
# else:
#     print(f"{number} is not greater than, or less than 5. Therefore, {number} must be equal to 5.")

# day = 'Friday'

# if day == "Monday":
#     print("Meeting at 9:00")
# elif day == "Wednesday":
#     print("Meeting at 2:00")
# elif day == "Friday":
#     print("Meeting at 4:00")
# else:
#     print("No meetings today")


#nested if-else

# exit_program = True
# manual_override = False
# critical_systems_shutdown = False

# if not exit_program and not critical_systems_shutdown:
#     if manual_override:
#         print("Shutting system down manually")
#     else:
#         print("This program will not exit just yet")
# elif exit_program and critical_systems_shutdown is not True:
#     print("Critical systems must be safely shut down before exiting the program")
# else:
#     print("This program will now be terminated...")


#Nested If/Else Statements Challenge
# admin = False
# update_required = True

# if admin == False:
#     print("You need admin privileges to do this")
# if update_required == True:
#     print("You are authorized to update") 
# else:
#     print("No update required")