from random import randint


def dofunc():
    # in this example, we simply use do,while to continue app as much as user wants to.
    try:
        print(f'Result is: {int(input("a:")) * int(input("b:"))}')  # print a*b
    except:
        print('Please only use integers!')  # a simple error catching!
    while input('Would you like to continue?').lower() == 'y':  # until the input is y, let the function continue!
        dofunc()


def cleardo():
    # in this example, we define a as a global variable to use it after the execution of function.
    global a  # declare the a variable as global
    a = int(input('number a :'))  # define it with an input

    while a < 5:  # we want a number that is less than number 5
        cleardo()


print("clearDo function's a variable:" + str(cleardo()))


def returndo():
    """in this example, we define a random number x, and we want function to
       produce it  until it s lower than 18. Then return |20-x|"""
    x = randint(0, 20)
    while x > 18:
        returndo()
    return abs(20 - x)  # absolute value of 20-x = | 20-x |


print('returnDo function returns:' + str(returndo()))
