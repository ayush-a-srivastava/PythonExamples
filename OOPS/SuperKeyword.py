class SuperExample:

    def display(self):
        print("This is a parent method")

class Child(SuperExample):

    def display(self):
        super().display()
        print("This is a child method")

child = Child()
child.display()