class employe:
    name = "Dipen"
    language = "python" # This is a class attribute
    salary = 1000000

Dipen = employe
Dipen.language = "django" # This is a object attribute
print(Dipen.name,Dipen.salary, Dipen.language)