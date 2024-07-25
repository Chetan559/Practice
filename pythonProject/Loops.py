#  In this program we'll see for, while  in python

def main1():
    number = get_number()
    meow(number)

def get_number():
    while True:  # infinite loop is resulted if we put True as a condition in a loop
        n = int(input("What's the number? "))
        if n<= 0:
            continue   # contiue is used to skip current iteration and goto next iteration
        elif n>0:
            break  # break is used to break out of loop
    return n

def meow(n):
     '''
     python doesn't have i++ or  i-- function os it doen't have for loops similar to C , Java 
      the syntax for for loop in python is given below i.e. for i in [0,1,2,3,....] (i.e. list) 
     instead of usnig list we can use range(n) funtion which increments i upto n ( i.e. i<n) 
     '''
     for _ in range(n):    
        print("meow")


main1()    