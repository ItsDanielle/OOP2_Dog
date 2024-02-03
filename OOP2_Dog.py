# Danielle Lockhart
# OOP Mini Project 2

class Dog:
    def __init__(self, age, name, is_male, weight):
        self.age = age
        self.name = name
        self.is_male = is_male # Boolean. True if Male, False if Female.
        self.weight = weight

Moe = Dog(age=1, name="Moe", is_male=False, weight=5)
my_dog = Moe

print(f"Name: {my_dog.name}, Age: {my_dog.age}, Weight: {my_dog.weight}, Gender: {'Male' if my_dog.is_male else 'Female'}")