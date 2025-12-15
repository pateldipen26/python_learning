class Employe:
    language = "python"
    salary = 1000000

    def __init__(self, name, salary, language):
        self.name = name
        self.salary = salary
        self.language = language
        print(" I am creating an object")

    
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("good morning ")

Dipen = Employe("Dipen", 2600000, "JS")
print(Dipen.name, Dipen.language, Dipen.salary)