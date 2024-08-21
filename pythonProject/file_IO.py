# here we'll see how to manipulate files in python 
# we'll use open function to open a file and perform an operation on it
def write_on_file():
    name = input("Enter the name: ")
    house = input("Enter the house: ")
    # the second argument is the operatio we're performing on the file
    '''
    file = open("name.txt", "a")
    file.write(f"{name}/n")
    # it is important to close a file afte performing an operation if it's not closed properly it may curropt the file
    file.close()
    '''
    # to overcome this problem we use "with" keyword to automatically open and close a file after the operation is performed
    # with 'operation' as 'variable_name'
    # .csv file is comma seperated file where words  are seperated by commas(,)
    with open("name.txt", "a") as file:
        file.write(f"{name},{house}\n")


# now we'll acess that file
def read_on_file():
    students = []

    with open("name.txt") as file:
        #  by defalut the operation is read operation
        for line in file:
            name, house = line.rstrip().split(",")
            student = {"name":name, "house":house}
            students.append(student)
    '''        
    def get_name(student):
        return student["name"]

    # here we're passing the funtion get_name as a parameter, this is how we sort th list of dictionary

    for student in sorted(students, key = get_name):
        print(f"{student['name']} lives in {student['house']}")
    '''
    # lambda is the key word which tells the compiler that it is a name less function
    #  after keyword lambda we write the argument and return value we want seperated by :
    # the above commented code and the code below are equivalent
    for student in sorted(students, key = lambda student : student["name"]):
        print(f"{student['name']} lives in {student['house']}")

write_on_file()   
read_on_file()