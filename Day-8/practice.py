# class program:
#     company = "GOOGLE"

#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

# z = program("Dipen", 2600000)
# print(z.name, z.company, z.salary)


class calculator:
    def __init__(self, n):
        self.n = n
    
    def square(self):
        print(f"The square is {self.n * self.n}")

    def cube(self):
        print(f"The cube is {self.n * self.n * self.n}")

    def squareroot(self):
        print(f"The squareroot is {self.n**1/2}")

a = calculator(40)
a.square()
a.cube()
a.squareroot()
   


# class Car:
#     def __init__(self,compney,model,color,fuel_type):
#         self.compney=compney
#         self.model=model
#         self.color=color
#         self.fuel_type=fuel_type


# # That part is abstraction in classs......
#     def car_detail(self):
#         print(f"Car Compney name is :{self.compney}\nCar Model is :{self.model}\nCar Colour is :{self.color}\nThat Car Fuel Type is :{self.fuel_type}\n ")

# p="Petrol"
# d="Diesel"
# c="Cng"
# e="Ev"
# car1=Car("BMW","M5","Black",p)
# car2=Car("Audi","RS e-tron","White",e)
# car3=Car("Honda","CIVIC","Silver",p)
# car4=Car("Mahindra","Scorpio s11","Black",d)

# car1.car_detail()
# car2.car_detail()
# car3.car_detail()
# car4.car_detail()