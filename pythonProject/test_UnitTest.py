# it is very inconvinient to test our code for each case instead we can automate our code by creating a test file
#  we can just import the function/pyton filewe want to test and pass the argument init and compare the return value using if else or try except block but by using that it will make testing more lengthy instead use 3rd party libreries availabe for this perpose

# we'll use "pytest" Librery to test our code 

import pytest 
from testfiles.calculator import square

# to test a function use "test_" at the start of that function or to test whole folder use "test_" at the start of file name and write your tests in that file also remmember to place __init__.py file in folder to test a folder using pytest because the presence on __init__.py file in a folder will be treated as a pakage

# to use pytest we run "pytest file_name.py" or "pytest folder_name" command in terminal

def test_square_positive():
    # arresert is a keyword in python which only accepts True boolean value if the value is Flase it will raise AssersionError
    assert square(2) == 4
    assert square(3) == 9
    assert square(4) == 16
    assert square(5) == 25
    
def test_square_negative():
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(-4) == 16
    assert square(-5) == 25
    
def test_square_decimal():
    # we can only have limited precision with decimal numbers so pytest has a approx funtion which allows very little tolerance for decimal values
    assert square(1.2) == pytest.approx(1.44)
    
def test_square_string():
    # raises is an function that comes with pytest to test the function and raise a error for certain argument, if the function raises the error it passes that test
    with pytest.raises(TypeError):
        square("string")
        
