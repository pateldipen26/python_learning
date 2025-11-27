d = {} #empty dictionary

marks = {
    "zalak" : 99,
    "dipen" : 97,
    "dharmi" : 50,
    "tejas" : 24
}

print(marks, type(marks))
print(marks["dipen"])

print(marks.items()) #giving the all valu in tuple form

print (marks.keys()) # show the key stored info

print (marks.values()) #show valu in keys

marks.update({"dipen" : 95, "zalak" : 100, "viajy" : 65}) #update the valu

print(marks.get("dipen")) # give the valu 
print(marks.get("vijay")) # not in valu get none


r=marks.pop("dharmi") # remove the specific valu
r=marks.popitem() # remove the last valu in dic
print(r)
print(marks)

cars = {
    "BUGATI" : "DUGATI",
    "TATA" : "BMW",
    "LAND_ROVER" : "KOENISEGG_JESKO"
}

car = input("enter the fastest car name :")

print(cars[car])

d = {}

name = input("enter frend name :")
lang = input("enter lang name :")
d.update({name: lang})
name = input("enter frend name :")
lang = input("enter lang name :")
d.update({name: lang})
name = input("enter frend name :")
lang = input("enter lang name :")
d.update({name: lang})
name = input("enter frend name :")
lang = input("enter lang name :")
d.update({name: lang})
name = input("enter frend name :")
lang = input("enter lang name :")
d.update({name: lang})

print(d)