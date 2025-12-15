class employe:
    name = "Dipen"
    language = "python" # This is a class attribute
    salary = 1000000

    def getInfo(self):
        print(f"the laguage is {self.language}. The salary is {self.salary}")
    
    @
    def greet(self):
        print("good morning")


Dipen = employe()
# Dipen.name = "Dipen" ## This is a object attribute
Dipen.getInfo()
Dipen.greet()
# print(Dipen.name,Dipen.salary, Dipen.language)