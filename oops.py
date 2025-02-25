# class car:
#     def __init__(self , Brand:str , Model:str , Year:int):
#         self.Brand = Brand
#         self.Model = Model
#         self.Year = Year
#         print("Object Created")

#     def startEngine(self):
#         print("Engine Start")

#     @classmethod
#     def instantiateThroughCSV(cls):
#         cars = []
#         import csv
#         with open("car.csv","r") as file :
#             rows = csv.reader(file)
#             next(rows)
#             for row in rows:
#                 # print(row)
#                 car = cls (
#                     Brand = row[0],
#                     Model = row[1],
#                     Year= row[2]
#                 )
#                 cars.append(car)
#         return cars

#     @staticmethod
#     def generalInfo():
#         print("Car is fit to run on road for 15 years")

# # car1 =  car("Toyota","Hilux",2022)
# # car1.startEngine()

# if __name__== "__main__":
#     cars =car.instantiateThroughCSV()
#     print(cars)
#     for i, c in enumerate(cars):
#             print(f"Car {i+1}:")
#             print(f"Brand: {c.Brand}")
#             print(f"Model: {c.Model}")
#             print(f"Year: {c.Year}")


# # inheritence 

# class Animal:
#     def __init__(self):
#         print("Animal Created")

#     def makeSound(self):
#         print(f"{self.name}is Making sound")

# class Mammal:
#     def __init__(self):
#         print("Mammal craeted")

#     def walk(self):
#         print(f"{self.name} is Walking")

# class Dog(Mammal , Animal):
#     def __init__(self , name):
#         super().__init__()
#         self.name = name
#         print("Dog Created")

# if __name__ == "__main__":
#         dog1 = Dog("Bruno")
#         print(dog1.name)

# # Polymorphism
# class scientifCalculator:
#     def add(self , a, b ,*args):
#         sum= a+b
#         for x in args:
#             sum += x
#         return sum


# class calculator(scientifCalculator):
#     def add(self , a, b, c=0 , d=0):
#         return a+b+c+d
    
#     def mul(self , a, b, c=0 , d=0):
#         return a*b*c*d
    
# if __name__ == "__main__":
#     calc = calculator()

#     # compile time polymorphism
#     calc.add(4,5)
#     calc.add(4,2,1)

#     # run time polymorphism
#     scalc = [scientifCalculator() , calc] 

#     for x in scalc:
#         print(x.add(4,5,6))
        
# # abstraction
# from abc import ABC , abstractmethod
# class Animal(ABC):

#     def __init__(self):
#         super().__init__()
#         print("Animal in process")
    
#     @abstractmethod
#     def makeSound(self):
#         pass
    
#     def walk(self):
#         pass

# class Dog(Animal):
    
#     def __init__(self):
#         super().__init__()
#         print("dog created")

#     def makeSound(self):
#         print("Dog Sound")
    
#     def walk(self):
#         print("Dog walking")

# if __name__ == "__main__":
#     dog1 = Dog()
