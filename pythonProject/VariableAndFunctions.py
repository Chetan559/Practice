# variable = a reusable container for storing a value
#                   a variable behaves as if it were the value it contains

# multiple assignment = assign multiple variable in a single line of code

name, age, height = "chetan", 19, 5.8

# the above line is equivalent of    name = "chetan"
#                                    age =19
#                                    height =5.8
# print(*objects, sep='', end='\n') is a function used to print in terminal
print(height)
print(age)
print(name)

#  type casting = The process of converting a value of one data type to another
#                          (string, integer, float, boolean)
#                          Explicit vs Implicit

# type(variable_name)  this funtion is used to determine the data type of a variable
print(type(name))
# int(variable_name), str(variable name) these function are type casting functions
print(type(height))
print(height)
height = int(height)
print(type(height))
print(height)
# input() is similar to scanf() function in c.
gname = input("give your name\n").title()
print(gname)

print(f"this is a formated string where {gname} is a varible ")

# -----------------------------------------------------------------------------------------------------------------------
# let us take a calculator example
x = float(input("enter your x:"))
y = float(input("enter your y:"))

z = x/y
print(z)
# here .2f is used to print only two decimal digits in z
print(f"{z:.2f}")