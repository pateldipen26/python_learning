def god():
    print("Good Day")
god()

def dip(name):
    print("good day," + name)
dip("dipen")

def bad(name, ending):
    print("good day," + name)
    print(ending)

bad("dipen", "how are you")
bad("zalu", "how are you")
bad("dharmi", "how are you")



def greatest(a, b, c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c

a = 22
b = 24
c = 20

print(greatest(a,b,c))

def pattern(n):
    if(n==0):
        return
    print("*" * n)
    pattern(n-1)

pattern(10)


def multiply(n):
    for i in range(1, 11):
        print(f"{n} X {i} = {n*i}")

multiply(48)