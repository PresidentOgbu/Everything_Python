# # This particuar file is created to teach lemaa the basics of python


# print ("Hello, world")
# name = "uchenna"
# print (name) 

# print ("The best school in the world is Havard University")

# school = "UNILAG is the best institute of learning in nigeria"
# print (school)


# 1. Write a script that creates the two variables, num1 and num2. Both
# num1 and num2 should be assigned the integer literal 25,000,000,
# one written with underscored and one without. Print num1 and num2
# on two separate lines.

# 2. Write a script that assigns the floating-point literal 175000.0 to the
# variable num using exponential notation, and then prints num in the
# interactive window.

# 3. In the interactive window, try and find the smallest exponent N so
# that 2e<N>, where <N> is replaced with your number, returns inf.


# 4. Write a script called exponent.py that receives two numbers from the
# user and displays the first number raised to the power of the second
# number.
# A sample run of the program should look like this (with example input
# that has been provided by the user included below):
# Enter a base: 1.2
# Enter an exponent: 3
# 1.2 to the power of 3 = 1.7279999999999998


# 1
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



# # 1. Print the result of the calculation 3 ** .125 as a fixed-point number
# # with three decimal places.
# # 2. Print the number 150000 as currency, with the thousands grouped
# # with commas. Currency should be displayed with two decimal
# # places.
# # 3. Print the result of 2 / 10 as a percentage with no decimal places.
# # The output should look like 20%.



# print(f"{3 ** .125:.3f}")


# # 1. Write a function called cube() with one number parameter and returns
# # the value of that number raised to the third power. Test the
# # function by displaying the result of calling your cube() function on
# # a few different numbers.
# # 2. Write a function called greet() that takes one string parameter
# # called name and displays the text "Hello <name>!", where <name> is
# # replaced with the value of the name parameter




# # 1. Write a script that asks the user to input a number and then displays
# # that number rounded to two decimal places. When run, your
# # program should look like this:
# # Enter a number: 5.432
# # 5.432 rounded to 2 decimal places is 5.43
# # 2. Write a script that asks the user to input a number and then displays
# # the absolute value of that number. When run, your program
# # should look like this:
# # Enter a number: -10
# # The absolute value of -10 is 10.0
# # 3. Write a script that asks the user to input two numbers by using the
# # input() function twice, then display whether or not the difference
# # between those two number is an integer. When run, your program
# # should look like this:
# # Enter a number: 1.5
# # Enter another number: .5
# # The difference between 1.5 and .5 is an integer? True!
# # If the user inputs two numbers whose difference is not integral,
# # the output should look like this:
# # Enter a number: 1.5
# # Enter another number: 1.0
# # The difference between 1.5 and 1.0 is an integer? False!



# num = input("Enter the number:")
# print(f"{num} rounded to 2 decimal places is round({num}, 2)")


# lee = input("Enter a number:")
# print(f"The absolute value of {lee} is {abs(float(lee))}")


# entry = input ("Enter a number")
# entry2 = input("Enter another number")

# print(f"the difference between {entry} and {entry2} is an integer? {float(entry) - float(entry2) % 1 == 0}")



# # 1. convert_cel_to_far() which takes one float parameter representing
# # degrees Celsius and returns a float representing the same temperature
# # in degrees Fahrenheit using the following formula:
# # F = C * 9/5 + 32
# # 2. convert_far_to_cel() which take one float parameter representing
# # degrees Fahrenheit and returns a float representing the same temperature
# # in degrees Celsius using the following formula:
# # C = (F - 32) * 5/9
# # The script should first prompt the user to enter a temperature in degrees
# # Fahrenheit and then display the temperature converted to Celsius.
# # Then prompt the user to enter a temperature in degrees Celsius and
# # display the temperature converted to Fahrenheit.
# # All converted temperatures should be rounded to 2 decimal places.
# # Here’s a sample run of the program:
# # Enter a temperature in degrees F: 72
# # 72 degrees F = 22.22 degrees C
# # Enter a temperature in degrees C: 37
# # 37 degrees C = 98.60 degrees F


# def convert_cel_to_far(celcius):
#     return celcius * 9/5 + 32
# celcius = float(input("Enter a temperature in degrees C: "))
# fahrenheit = convert_cel_to_far(celcius)
# print(f"{celcius} degrees C = {fahrenheit:.2f} degrees F")



# def convert_far_to_cel(fahrenheit):
#     return (fahrenheit - 32) * 5/9
# fahrenheit = float(input("Enter a temperature in degrees F:"))
# celcius = convert_far_to_cel(fahrenheit)
# print(f"{fahrenheit} degrees F = {celcius:.2f} degrees C")




# The while Loop
# while loops repeat a section of code while some condition is true.
# There are two parts to every while loop:
# 1. The while statement starts with the while keyword, followed by a
# test condition, and ends with a colon (:).
# 2. The loop body contains the code that gets repeated at each step
# of the loop. Each line is indented four spaces.


# n = 1
# while n <= 5:
#     print(n)
#     n += 1 # (n=n+1)



# for letter in "boy":
#     print(letter)   



word = "Python"
index = 0
while index < len(word):
    print(word[index])
index = index + 1




1. Write a for loop that prints out the integers 2 through 10, each on
a new line, by using the range() function.
2. Use a while loop that prints out the integers 2 through 10 (Hint:
You’ll need to create a new integer first.)
3. Write a function called doubles() that takes one number as its input
and doubles that number. Then use the doubles() function in a
loop to double the number 2 three times, displaying each result on
a separate line. Here is some sample output:
4
8
16




In this challenge, you will write a program called invest.py that tracks
the growing amount of an investment over time.
An initial deposit, called the principal amount, is made. Each year,
the amount increases by a fixed percentage, called the annual rate of
return.
For example, a principal amount of $100 with an annual rate of return
of 5% increases the first year by $5. The second year, the increase is
5% of the new amount $105, which is $5.25.
Write a function called invest with three parameters: the principal
amount, the annual rate of return, and the number of years to calculate.
The function signature might look something like this:
def invest(amount, rate, years):
The function then prints out the amount of the investment, rounded
to 2 decimal places, at the end of each year for the specified number
of years.
For example, calling invest(100, .05, 4) should print the following:
year 1: $105.00
year 2: $110.25
year 3: $115.76
year 4: $121.55
To finish the program, prompt the user to enter an initial amount, an
annual percentage rate, and a number of years. Then call invest() to
display the calculations for the values entered by the user.