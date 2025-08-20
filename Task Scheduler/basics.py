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



#1
num1 = 25000000
num2 = 25_000_000
print(num1)
print(num2)

#2

num = 1.75e5
print(num)


#3

num = 2e308
print(num)


#4


# Write a script called exponent.py that receives two numbers from the
# user and displays the first number raised to the power of the second
# number.
# A sample run of the program should look like this (with example input
# that has been provided by the user included below):
# Enter a base: 1.2
# Enter an exponent: 3
# 1.2 to the power of 3 = 1.7279999999999998


base = float(input("Enter a base:"))
exponent = float(input("Enter an exponent:"))

result = base ** exponent
print(result)
print(f"{base} to the power of {exponent} = {result}")
