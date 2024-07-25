#  IN this program we'll see list , dictionary and list of dictionary in Python

#  list in python is collection of dictint items which starts(i.e. indexes) from 0
'''
 suppose we want to implement list of students in vgec we can do it as given below
'''
def lists():
    print("List of student:")
    L_students = ["Chetan","Mahendra","Sudhanshu"]
    iterate1(L_students)  # prints all the elements in list
    #  now if we want to add an element in list we can do it by append(element) function
    L_students.append("Vyom")
    iterate1(L_students)
    #  now if we want to remove an item form list we can do it by usnig remove(elemnet) function
    L_students.remove("Chetan")  # finds and removes Chetan from list
    L_students.remove("Mahendra")
    L_students.remove("Sudhanshu")
    iterate1(L_students)
    L_students.append(["Sudhanshu", "Chetan",  "Mahendra"])
    iterate1(L_students)  # here the append function will add whole list as single element which is sometimes not desired
    L_students.remove(["Sudhanshu", "Chetan",  "Mahendra"])
    L_students.extend(["Sudhanshu", "Chetan",  "Mahendra"]) # list1.extend(list2) will append each elements of list2 into list1 one by one
    iterate1(L_students)
    L_students.reverse() # reverse() function will reverse the order of elements in list
    iterate1(L_students)
    L_students.remove("Chetan")  
    L_students.insert(0,"Chetan") # this will insert Chetan at 0th position in list
    iterate1(L_students)


def iterate1(L_students):
    for i in range(len(L_students)):  # len(list) returns the number of items in list
        print(i + 1, L_students[i])
    print()

lists()
'''
Suppose a user wants to implement a table in python
        name  |     division
--------------+-------------------------
    Chetan    |     H2
--------------+-------------------------
    Mahendra  |     H3
--------------+-------------------------
    Sudhanshu |     H2
--------------+-------------------------
    Vyom      |     G3

    we can implement above table in python using dictionary. dictionary is collection of pair of key and value
'''
print()
print("Dictionary implementation for data set of students and their division")
print()

def Dictionary():
    D_students = {
        "Chetan" : "H2"
        #  key : value pairs
     }
    iterateD(D_students)
    D_students["Mahendra"] = "H3"  # this is the way to add a key and its value to dictionary
    D_students.update({"Sudhanshu" : "H2", "Vyom" : "G3"}) # .update(Dictionary) add all key and value pair into the Dictionary one-by-one
    iterateD(D_students)

    
def iterateD(D_students):
    
    for student in D_students.keys():  # .key() is used to return keys in Dictionary
        print(student,end=" ")
    print()
    
    for division in D_students.values():  # .values() is used to return values in Dictionary
        print(division,end=" ")
    print()
    print()

    for student in D_students:
        print(student, D_students[student],sep =" -> ")
        # student is the key here and by passing the key to list we can print value associated to the key
    print()

Dictionary()
'''
suppose we wnat to implement the data set given below consisiting of name, division, city and desired profession of student
        Name        |   Division    |   City        |   D_Profession
    ----------------+---------------+---------------+------------------
        Chetan      |       H2      |   Ahmedabad   |   Data Engineer
    ----------------+---------------+---------------+------------------
        Mahendra    |       H3      |   Bhavnagar   |   SDE
    ----------------+---------------+---------------+------------------
        Sudhanshu   |       H2      |   Gandhinagar |   None
    ----------------+---------------+---------------+------------------
        Vyom        |       G3      |               |   MBA
    ----------------+---------------+---------------+------------------
  
    We can implement and access above data by using list of dictionary
'''    
print()
print("Implementation of Data set consisiting of name, division, city and desired profession of student")
print()

def ListOfDictionary():
    LoD_students = [
        {"name":"Chetan", "Division":"H2", "City":"Ahmedabad", "D_Profession":"Data Engineer"},
        {"name":"Mahendra", "Division":"H3", "City":"Bhavnagar", "D_Profession":"SDE"},
        {"name":"Sudhanshu", "Division":"H2", "City":"Gandhinagar", "D_Profession":None}, # None is special key word iun python which is used to discribe no value
        {"name":"Vyom", "Division":"G3", "D_Profession":"MBA"}
        #  here each dictionary has 4 keys name, Division, City, D_Profession and their value asigned to it
        # all dictionary have same keys but different values
    ]
    iterateLoD(LoD_students)

def iterateLoD(LoD_students):
    for student in LoD_students:
        #  student acts as a iterator which iterates to each element(here dictionary) in the list 
        print(student["name"], student["Division"], student.get("City", "Unkonwn"), student["D_Profession"], sep = " -> ")
        # .get(key , message) checks if key extis and if it does exist it returns its value .otherwise it returns the message
        #  here 1st the iterator visits each dictionary and returns the value asigned tho the key 

ListOfDictionary()
'''
summary:
    List                ->      [.,.,.,.,.,.,.,.]
    Dictionary          ->      {.,.,.,.,.,.,.,.}
    List of Dictionary  ->  [                                              | . -> elements or pair of (key:vaule)
                                {.,.,.,.,.,.,.,.},                         | , -> seperate each elements
                                {.,.,.,.,.,.,.,.},
                                {.,.,.,.,.,.,.,.}
                            ]

'''