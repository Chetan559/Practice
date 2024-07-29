'''
In this program we'll see try and except statement in Python which are used for error handling
'''


Calories = {
    "Apple" : "130",
    "Avocado" : "50",
    "Banana" : "110",
    "Cantaloupe" : "50",
    "Grapefruit" : "60",
    "Grapes" : "90",
    "Honeydew Melon" : "50",
    "Kiwifruit" : "90",
    "Lemon" : "15",
    "Lime" : "20",
    "Nectarine" : "60",
    "Orange" : "80",
    "Peach" : "60",
    "Pear" : "100",
    "Pineapple" : "50",
    "Plums" : "70",
    "Strawberries" : "50 kcal",
    "Sweet Cherries" : "100",
    "Tangerin" : "50",
    "Watermelon" : "80"
}

def main():
    # the try statement contais all the part of code which may produce some error
    #  make sure to use try statement with less no. of code as much as possible 
    while True:
        try:
            fruit = input("Fruit: ")
            print("Calories:",int(Calories[fruit]))
        # except statemet is used to handel the eception occured in try statement
        except ValueError:
            print(f"Can't convert {Calories[fruit]} into Integer")  
        except KeyError:
            #  user can use "pass" keyword if they dont want to do anything with the error. i.e. bypass the handling part
            pass 
        except Exception as e: # if we don't know which error may occur we can use "Exeption as e" and by print the we can tell user which error has occured
            print(f"There is a {e} Exception") 
        # the else statement used with try and except statement will only execute after the try statement has successfully executed without thowing any exeption
        else:  
            break
        
main()