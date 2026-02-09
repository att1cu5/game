# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run i
x=int(input())
y=int(input())
z=int(input())

b=(x*y)+(y*z)+(z*x)
print(b)
for i in range(0,x):
    for i in range(0,y*4):
         print("\\",end="")
    for i in range(0,y):
        print("\\",end="")
    for i in range(0,y):
        print("=",end="")
    for i in range(0,y):
        print("/",end="")
    for i in range(0,y*4):
         print("/",end="")
    print()
for i in range(0,x):

    for i in range(0,y):
        print("| | |",end="")
    for i in range(0,y):
        print("X",end="")
    for i in range(0,y):
        print("| | |",end="")
    print()
for i in range(0,x):
    for i in range(0,x*4):
        print("/",end="")
    for i in range(0,y):
        print("/",end="")
    for i in range(0,y):
        print("=",end="")
    for i in range(0,y):
        print("\\",end="")
    for i in range(0,x*4):
        print("\\",end="")
    print()
