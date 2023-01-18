b=45
def a():
    b=34
    print(b)

a()
print(b)

def m():
    global b
    b=100
    print(b)

    
m()
print(b)