# This particuar file is created to teach lemaa the basics of python


# print (Hello, world)
# name = "uchenna"
# print (name) 

print ("The best school in the world is Havard University")

school = "UNILAG is the best institute of learning in nigeria"
print (school)


# 1. Write a script that creates the two variables, num1 and num2. Both
# num1 and num2 should be assigned the integer literal 25,000,000,
# one written with underscored and one without. Print num1 and num2
# on two separate lines.

# 2. Write a script that assigns the floating-point literal 175000.0 to the
# variable num using exponential notation, and then prints num in the
# interactive window.

# 3. In the interactive window, try and find the smallest exponent N so
# that 2e<N>, where <N> is replaced with your number, returns inf.


#4. Write a script called exponent.py that receives two numbers from the
# user and displays the first number raised to the power of the second
# number.
# A sample run of the program should look like this (with example input
# that has been provided by the user included below):
# Enter a base: 1.2
# Enter an exponent: 3
# 1.2 to the power of 3 = 1.7279999999999998


# #1
# num1 = 25000000
# num2 = 25_000_000
# print(num1)
# print(num2)

# #2

# num = 1.75e5
# print(num)


# #3

# num = 2e308
# print(num)





# base = float(input("Enter a base:"))
# exponent = float(input("Enter an exponent:"))

# result = base ** exponent
# print(result)
# print(f"{base} to the power of {exponent} = {result}")



# 1. Print the result of the calculation 3 ** .125 as a fixed-point number
# with three decimal places.
# 2. Print the number 150000 as currency, with the thousands grouped
# with commas. Currency should be displayed with two decimal
# places.
# 3. Print the result of 2 / 10 as a percentage with no decimal places.
# The output should look like 20%.


# 1. print ()




# 1. Write a function called cube() with one number parameter and returns
# the value of that number raised to the third power. Test the
# function by displaying the result of calling your cube() function on
# a few different numbers.
# 2. Write a function called greet() that takes one string parameter
# called name and displays the text "Hello <name>!", where <name> is
# replaced with the value of the name parameter




# 1. Write a script that asks the user to input a number and then displays
# that number rounded to two decimal places. When run, your
# program should look like this:
# Enter a number: 5.432
# 5.432 rounded to 2 decimal places is 5.43
# 2. Write a script that asks the user to input a number and then displays
# the absolute value of that number. When run, your program
# should look like this:
# Enter a number: -10
# The absolute value of -10 is 10.0
# 3. Write a script that asks the user to input two numbers by using the
# input() function twice, then display whether or not the difference
# between those two number is an integer. When run, your program
# should look like this:
# Enter a number: 1.5
# Enter another number: .5
# The difference between 1.5 and .5 is an integer? True!
# If the user inputs two numbers whose difference is not integral,
# the output should look like this:
# Enter a number: 1.5
# Enter another number: 1.0
# The difference between 1.5 and 1.0 is an integer? False!



# num = input("Enter the number:")
# print(f"{num} rounded to 2 decimal places is round({num}, 2)")


# lee = input("Enter a number:")
# print(f"The absolute value of {lee} is {abs(float(lee))}")


entry = input ("Enter a number")
entry2 = input("Enter another number")

print(f"the difference between {entry} and {entry2} is an integer? {float(entry) - float(entry2) % 1 == 0}")

