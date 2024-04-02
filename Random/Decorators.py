def say_hi(func):
    def wrapper():
        print("First say Hi")
        func()
    return wrapper

@say_hi
def hello():
    print("Hello Ayush")


hello()