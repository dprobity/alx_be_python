# # class Car:
# #     def __init__(self,make,model,year):
# #         pass


# class Dog:
#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed
    

#     def brak(self):
#         return "Woof"

# dog1 = Dog("Buddy","Golden Retriever")
# dog2 = Dog("Max", "German Shephered")

# # Accessing properties and methods of a an object 
# print(f"{dog1.name} is a {dog1.breed}. He says {dog1.brak()}")
# print(f"{dog2.name} is a {dog2.breed}. He says {dog2.brak()}")

class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        pass

class Lion(Animal):
    def speak(self):
        return f"{self.name} the Lion roars"
    
class Elephant(Animal):
    def speak(self):
        return f"{self.name} the Elephant trumpets"
    


# Polymorphism

zoo = [ 
    Lion("Simba"),
    Elephant("Dumbo")


]

for animal in zoo:
    print(animal.speak())