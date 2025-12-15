class employe:
    name = "Dipen"
    language = "python" # This is a class attribute
    salary = 1000000

Dipen = employe
Dipen.name = "Dipen" # This is a object attribute
print(Dipen.name,Dipen.salary, Dipen.language)

zalak = employe
zalak.name = "zalak"
print(zalak.name,zalak.salary, zalak.language)

#  Here name is instance attribute and salary and language are class attributes as they directly belong to the class