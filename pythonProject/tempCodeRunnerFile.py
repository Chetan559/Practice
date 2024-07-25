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
    
    for student in D_students.keys():
        print(student,end=" ")
    print()
    
    for division in D_students.values():
        print(division,end=" ")
    print()

    for student in D_students:
        print(student, D_students[student],sep =" -> ")
        # student is the key here and by passing the key to list we can print value associated to the key
    print()

Dictionary()