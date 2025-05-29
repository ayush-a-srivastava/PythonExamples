count = 10
class MyClass:
    count = 20

    def add(self):
        count = 30
        print("Local variable : ", count)
        print("Class variable: ", MyClass.count)
        print("Global variable: ", globals()['count'])


myclass = MyClass()
myclass.add()