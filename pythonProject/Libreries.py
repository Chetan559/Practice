#  in this program we'll see about pakages, libraries and APis
# libraries are some files of python program previously written by some other user we can import those libreries and use its function and variebles in our program
import sys
#  the import keyword will map all the function and variesble to this file
from random import choice, randint
#  the from keyword will import particular function and variable instead of whole file
import cowsay
#  here cowsay is not an inbuilt librery it's a 3rd party library which is called a Pakage. generally available at pypi.org
# python has its own inbuild pakages that is modules implemented in folders
#  to use a pakage in your file yopu need to install that pakage in you machine using pakage manager (python has its own called pip)


if len(sys.argv) != 2:
    sys.exit("Give 2 arguments. e.g. python Libreries Chetan")
# when you import whole module/file in a program you need to use dot(.) operator to use the functions and variable of that module/file
# argv is a command line argument which is given by the user at the time of running the file
#  eg:- python Libreies.py "Chetan Sharma"
#  thr argv[0] is the file name itself and if we don't use ""  in above example the program will treat Chetan and Sharma as two different element 
# argv is variable(list) and exit is a function in sys  module/file
wish = choice(["Afternoor", "Evening", "Night"])
# the advantage of using from keyword is that we don't need to use dot(.) operater. we can directly use the variable or function of that module/file just by using its name
print("Hello,",sys.argv[1],"Good",wish)

cowsay.cow("Hello" + sys.argv[1])
cowsay.trex("Hello" + sys.argv[1])
# these are funtion of pakage cowsay. refer to the documentations of the pakages if needed so