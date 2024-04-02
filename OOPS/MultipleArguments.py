class Argu:

    def __init__(self,*args):
        if(len(args)==2):
            self.ans = args[0] + args[1]

        elif isinstance(args[0],float):
           self.ans =0
           for i in args:
               self.ans+=i

        elif isinstance(args[0],str):
            self.ans = "Hello" + args[0] + "."


a1 = Argu(1,2)
print("Sum is: " ,a1.ans)
a2 = Argu(10.2,2.4,3.5)
print("Product is: ",a2.ans)
a3 = Argu(" Ayush")
print(a3.ans)
