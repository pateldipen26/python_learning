l = [26, "dipen", 22, "zalak","dharmi","vijay"]

i = 0

while(i<len(l)):
    print(l[i])
    i-=1

## they are used for odd number

i = 1
while i<=100:
    if(i%2 == 0):
        i += 1
        continue
    print(i)
    i += 1

## for the even number

i = 0
while i<=100:
    if(i%2 != 0):
        i += 1
        continue
    print(i)
    i += 1 


## give the factorial of number using while 
n = int(input("enter the number :"))
fact = 1
i = 1

while i <= n:
    fact *= i
    i += 1
print("factorial =", fact)

n = int(input("enter the number :"))
fact = 1

for i in range(1, n+1):
    fact *= i
print("factorial :", fact)