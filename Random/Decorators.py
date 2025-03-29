# '''
# Decorators are a way to modify the behaviour of functions and methods without changing the actual code.
# They allow you to add functionality to an existing definition dynamically
# '''
#
# # def say_hi(func):
# #     def wrapper():
# #         print("First say Hi")
# #         func()
# #     return wrapper
# #
# # @say_hi
# # def hello():
# #     print("Hello Ayush")
#
# # hello()
#
# def print_add(func):
#     print("Inside print_add")
#     def wrapper(*ar):
#         print("Total sum: ")
#         res = func(*ar)
#         return res
#     return wrapper
#
# @print_add
# def add(a,b,c,d):
#     print("Add called")
#     return a+b+c+d
#
# print(add(2,3,4,5))
#
#
# # def say(func):
# #     def wrapper():
# #         print("Before printing")
# #         func()
# #         print("After printing")
# #     return wrapper
# #
# # @say
# # def hello():
# #     print("Hello")
# #
# # hello()
#
#
# def print_convertString(func):
#     print("I am the first to print")
#     def wrapper(my_str):
#         print("I am the second")
#         res = func(my_str)
#         return res
#     return wrapper
#
# @print_convertString
# def convert_string(my_str):
#     print("The converted string is: ")
#     return my_str.lower()
#
#
# print(convert_string("AYUSH"))
#
#
#

def greet_hello(func):
    def wrapper():
        print("Hello !!!!")
        func()
        print("Nice to meet you.")
    return wrapper
@greet_hello
def say_hello():
    print("My name is Ayush")

say_hello()
