for i in range(1, 1000):
    print(i)

## for loops with lists

p = [2, 4, 6, 26, 24, 22, 2226]

for i in p:
    print(i)

##  for loop with tuples

z = (22, 26, 204, 209, 262)
for i in z:
    print(i)

## for loop with string

d = "dipen"

for i in d:
    print(i)

for i in range(1000):
    if(i == 544):
        break  # exit the loop right now 
    print(i)


for i in range(1000):
    if(i == 544):
        continue # skip the classifed value
    print(i)

d = int(input("enter the number :"))

for i in range (1, 11):
    print(f"{d} X {i} = {d * i}")
    
# value form the indx 

tup = (22, 26, 28, 32, 34)

for i in tup:
    print(i)

str = "dipenpatel"

for i in str:
    print(i)

str = "pateldipen"

for i in str:
    if (i == 'l'):
        print("l found") # searching the value and end the code
        break
    print(i)
else:
    print("END")    

num = [22, 3, 26, 36, 77, 88, 44, 26]

x = 26

idx = 0

for i in num:
    if (i == x):
        print("number is found :", idx)
    idx += 1

for i in range(1, 100, 2):
    print(i)

a = int(input("enter the start number :"))
b = int(input("enter the end number :"))

for i in range(a,b+1):
    print(i)