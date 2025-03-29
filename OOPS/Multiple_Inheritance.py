class A:

    def first(self):
        print("I am from first parent.")

class B(A):

    def second(self):
        super().first()
        print("I am from second parent")

class C(B,A):
    def child(self):
        super().second()
        print("I am the Child")

ch = C()

# ch.first()
# ch.second()
ch.child()