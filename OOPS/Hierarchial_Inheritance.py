class Electronics:

    def __init__(self,brand):
        self.brand = brand

    def show_brand(self):
        print(f'Brand: ',self.brand)

class Mobile(Electronics):

    def __init__(self,brand, RAM):
        Electronics.__init__(self,brand)
        self.RAM = RAM

    def mobile_details(self):
        print(f'{self.brand} has {self.RAM} GB RAM.')


class Laptop(Electronics):

    def __init__(self,brand, processor):
        super().__init__(brand)
        self.processor = processor

    def laptop_details(self):
        print(f'{self.brand} has {self.processor} processor.')

mo = Mobile("Samsung", 8)
lap = Laptop("Dell","i7")

mo.show_brand()
mo.mobile_details()
lap.show_brand()
lap.laptop_details()