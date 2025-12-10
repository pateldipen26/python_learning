a = int(input("enter the number :"))

if(a%2 ==0 and a%3 ==0):
    print("the number is devided buy both")
elif(a%2 ==0):
    print("the number is devided buy two")
elif(a%3 ==0):
    print("the number is devided buy three")
else:
    print("this number is or")


# # check number positive,negative or zero

a = int(input("enter the number :"))

if (a == 0):
    print("number is zero")
elif(a>=0):
    print("the number is positive")
else:
    print("the number is negative")

# # check age for voteing

z = int(input("enter your age :"))

if (z>=18):
    print("you are able for voting")
else:
    print("you are not able for voting")

# # number even or odd

d = int(input("enter the number :"))

if(d%2==0):
    print("the number is even :", d)
else:
    print("the number is odd :", d)

# # marksheet

p = int(input("ENTER YOUR MARKS :"))

if(p<=100 and p>=90):
    print("YOUR GRADE IS A")
if(p<=90 and p>=80):
    print("YOUR GRADE IS B")
if(p<=80 and p>=70):
    print("YOUR GRADE IS C")
if(p<=70 and p>=60):
    print("YOUR GRADE IS D")
if(p<=60 and p>=50):
    print("YOUR GRADE IS E")
if(p<=50):
    print("YOU ARE FAIL")

# # # check number bigger

a = int(input("enter number 1:"))
b = int(input("enter number 2:"))

if(a>b):
    print("the 1 number is biger")
else:
    print("the 2 number is bigger than number 1")

a = int(input("enter number 1 : "))
b = int(input("enter number 2 : "))
c = int(input("enter number 3 : "))

if(a>b):
    print("number one is biggest :", a)
elif(b>c):
    print("number two is biggest :", b)
else:
    print("number three is biggest :", c)

i = 1

while (i < 1000):
    print(i)
    i += 5

l = ["Dipen","Zalak","Dharmi","tejas","vijay","Dhruv"]

for name in l:
    if(name.startswith("D")):
        print(f"hello {name}")

## while for table

d = int(input("enter the number :"))

i = 0

while(i<11):
    if(d <= 0):
        print(f"{d} * {i} =", d*i)

        i += 1
    else:
        print(d,"the number is not available")
        break


a = int(input("enter the number 1:"))
b = int(input("enter the number 2:"))
c = int(input("enter the number 3:"))

if(a>b and a>c):
    print("the a is bigger")
elif(b>c ):
    print("the b is bigger")
else:
    print("the c is bigger")
 
z = int(input("Enter the number :"))

for i in range(2, z):
    if(z%i) ==0:
        print("number is not prime :",z)
        break
    else:
        print("the number is prime :", z)

rows = 5
for i in range(1, rows + 1):
    print(' ' * (rows - i) + '*' * (2 * i - 1))

d = int(input("enter the age :"))

if(d>=18):
    print("you are elibele for voting :",d)
else:
    print("you are not eliegble for voting :", d)

purchase = float(input("Enter the purchase amount: "))

if purchase >= 1000:
    discount = purchase * 0.20   # 20% discount
elif purchase >= 500:
    discount = purchase * 0.10   # 10% discount
else:
    discount = 0                 # no discount

final_price = purchase - discount

print("Discount:", discount)
print("Final Price:", final_price)


z =int(input ("""
        January : 1
        February : 2
        March : 3
        April : 4
        May : 5
        June : 6 
        July : 7
        August : 8
        September : 9 
        October : 10
        November : 11
        December : 12
          
        enter your choice:"""))
if (z == 1):
    print(z,"has 31 days")
elif (z == 2):
    year = int(input("enter year :"))
    if(year%4==0):
        print(z,"has 29 days",year,"tuje kiyya lena dena")
    else:
        print(z,"has 28 days")
elif (z == 3):
    print(z,"has 31 days")
elif (z == 4):
    print(z,"has 30 days")
elif (z == 5):
    print(z,"has 31 days")
elif (z == 6):
    print(z,"has 30 days")
elif (z == 7):
    print(z,"has 31 days")
elif (z == 8):
    print(z,"has 31 days")
elif (z == 9):
    print(z,"has 30 days")
elif (z == 10):
    print(z,"has 31 days")
elif (z == 11):
    print(z,"has 30 days")
elif (z == 12):
    print(z,"has 31 days")




        