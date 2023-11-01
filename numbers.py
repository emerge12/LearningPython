# - Python and numbers: Addition, Subtraction, Division, and Multiplication
Addition  = 2 + 6
print(Addition)

Subtraction  = 22 - 6
print(Subtraction)

Division  = 12 / 6
print(Division)

Multiplication  = 2 + 6
print(Multiplication)

#- Python uses two multiplication symbols to represent an exponent

exponent = 6**6
print(exponent)

#- Python calls every decimal number a float
#- Division of any two numbers i python will result in a float, even numbers that result in whole numbers
# - If an interger and a float is mixed in any operation, the result will be a float
# - Python defaults to a float in any operation that uses a float, even if the output is a whole number

float_number = 3*0.1
print(float_number)

float_number = 3/3
print(float_number)

mix_numbers = 3 + 3.0
print(mix_numbers)

# - When writing long numbers python allows you to used underscores to make large number more readable

underscore_number = 13_000_000_000
print(underscore_number)


# - Python does not have built-in costant type, however, when python programmers want to treat a number like a constant, it makes the variable all caps
MAX_CONNECTION = 500
print(MAX_CONNECTION)


my_fav_number  = 7
print(f"My favorite number is  {str(my_fav_number)}")