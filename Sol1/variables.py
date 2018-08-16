# declaring variables

foo = 123
print(foo)

#re-declare variable
#foo = 'abc'
#print(foo)

print('value of foo is:'+ str(123))

#global variable
def printFoo():
    global f
    f = "gFoo"
    print(f)

printFoo()
print (f)

#delete
del f
print (f)