class Parent:

    def parent_method(self):
        print("I am from parent class")

class Child(Parent):

    def child_method(self):
        super().parent_method()
        print("I am from Child class")

c = Child()
c.child_method()
# c.parent_method()