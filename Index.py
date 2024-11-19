""" Object-Oriented Programming (OOP) is a programming paradigm that
uses objects and classes to structure code. Python supports OOP and
provides several features to help you implement it, such as
classes, inheritance, encapsulation, polymorphism, and abstraction."""


# Defining a class start
class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


    def description(self):
        return f"{self.year} {self.make} {self.model}"


my_car = Car("Toyota", "Corolla", 2020)
print(my_car.description())

# Defining a class End

# Constructor Start

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")

dog1 = Dog("Buddy", 3)
dog1.bark()


# Constructor End




# Inheritance start


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")


class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks")

dog = Dog("Buddy")
dog.speak()


# Inheritance End



# Encapsulation Start

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())

# Encapsulation End


# Polymorphism Start

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

# Creating objects
dog = Dog()
cat = Cat()

dog.speak()
cat.speak()



# Polymorphism End



# Abstraction Start

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Dog barks")

dog = Dog()
dog.speak()

# Abstraction End









