gang = ["dipen", "zalak", 22, 26.07, "tejas", "priya"]

print(gang[0])

gang [0]= "vagadiya"
print(gang[0])

#list slicing

print(gang[0:4])

#add anything in list

gang.append("dharmi") 
print(gang)

# list sort number

d1 = [1 , 5 , 80 , 26 , 22 ,56]

d1.sort()

d1.reverse()# list reverse counting 

d1.insert(4, 4657) #insert new valu

d1.pop(3) # pop index number using for remove 
print(d1.pop(5)) #remov valu and highlight

d1.remove(22) # specfic valu for remove

print(d1)

car = []

c1 = input("enter car name: ")
car.append(c1)
c2 = input("enter car name: ")
car.append(c2)
c3 = input("enter car name: ")
car.append(c3)
c4 = input("enter car name: ")
car.append(c4)
c5 = input("enter car name: ")
car.append(c5)
c6 = input("enter car name: ")
car.append(c6)

print(car)


marks = []

m1 = int(input("enter marks here: "))
marks.append(m1)
m2 = int(input("enter marks here: "))
marks.append(m2)
m3 = int(input("enter marks here: "))
marks.append(m3)
m4 = int(input("enter marks here: "))
marks.append(m4)
m5 =int(input("enter marks here: "))
marks.append(m5)
m6 =int(input("enter marks here: "))
marks.append(m6)

marks.sort()

print(marks)


D = [85,99,995,889,45,685]

print(sum(D))