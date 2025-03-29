class Animal:

    def speak(self):
        print("Animal makes a sound")

class Mammal(Animal):

    def has_fur(self):
        print("Mammal has fur.")

class Dog(Mammal):

    def bark(self):
        print("Dogs can bark")

d = Dog()
d.speak()
d.has_fur()
d.bark()