# variable = a reusable container for storing a value
#                   a variable behaves as if it were the value it contains

# multiple assignment = assign multiple variable in a single line of code

name, age, height = "chetan", 19, 5.8

# the above line is equivalent of    name = "chetan"
#                                    age =19
#                                    height =5.8

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
