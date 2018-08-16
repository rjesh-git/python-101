# Functions

# function - no args

def someFunction():
    print('something from someFunction')

# function - with args
def square(number):
    return number*number

# function - with multiple args
def area(height,width):
    return height*width

# function - with variable number of args
def addAll(*args):
    rVal = 0
    for i in args:
        rVal = rVal + i
    return rVal

someFunction() #some function
print(square(16))
print('area is:',area(5,10))
print('area is:',area(width=100, height=20))
print('addAll:',addAll(1,2,3,4,5,6))