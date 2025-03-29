from abc import ABC, abstractmethod


# Abstract class
class PaymentMethod():

    def __init__(self,amount):
        self.amount = amount


    # Must be implemented by the child classes
    @abstractmethod
    def make_payment(self):
        pass

class creditCard(PaymentMethod):

    def __init__(self,amount, cardnumber):
        super().__init__(amount)
        self.cardnumber = cardnumber

    def make_payment(self):
        print(f'Rs {self.amount} is paid by using credit card number {self.cardnumber[-4:]}')


class UPI(PaymentMethod):

    def __init__(self, amount, UPIid):
        super().__init__(amount)
        self.UPIid = UPIid

    def make_payment(self):
        print(f'Rs {self.amount} is paid by using UPI ID {self.UPIid}')

class Paypal(PaymentMethod):

    def __init__(self, amount, paypal_mail):
        super().__init__(amount)
        self.paypal_mail = paypal_mail

    def make_payment(self):
        print(f'Rs {self.amount} is paid by using paypal mail id {self.paypal_mail}')


card = creditCard(4000, "2030-4567-1234-2087")
upi = UPI(5000,"897823@upi")
pay = Paypal(10000,"pay@test.com")

card.make_payment()
upi.make_payment()
pay.make_payment()