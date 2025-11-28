z = {22,26,25,56,85,22,26, "dipen", "zalak"}

d = set()

print(z, type(z))

z.add(2607) # add any valu in set

z.remove(85) # removing any value

print(z,type(z))

# union set using for the comabine two set 

d1 = {22,26,23,57,78}
d2 = {78,56,46,44,5}

print(d1.union(d2)) 

print(d1.intersection(d2)) # using for the scaning same number or value

v = d1.copy() #copy the value
print(v)

d3 = {"BMW","DUCATI","PAGANI","BUGATI","LAND_ROVER","KOENISEGG_JESKO","ASTON_MARTIN","MC_LAREN","PORSCHE","RIMAC_NEVERA","PININFARINA_BATTISTA","LAMBORGHINI_SIAN","FERRARI","MASERATI_MC20"}
print (d3.pop())

# practice set
s = set()

n = input("enter the number :")
s.add(int(n))
n = input("enter the number :")
s.add(int(n))
n = input("enter the number :")
s.add(int(n))
n = input("enter the number :")
s.add(int(n))
n = input("enter the number :")
s.add(int(n))
n = input("enter the number :")
s.add(int(n))
n = input("enter the number :")
s.add(int(n))

print(s)

z = set()

z.add(26)
z.add("26")

print(z)