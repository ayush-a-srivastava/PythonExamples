class Vehicle:

    color = "White"
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    pass

School_bus = Bus("Volvo",270,150)
School_bus1 = Bus("Mercedes",250,200)
print(School_bus.color, School_bus.name, School_bus.max_speed, School_bus.mileage)
print(School_bus1.color, School_bus1.name, School_bus1.max_speed, School_bus1.mileage)
print(type(School_bus))
print(isinstance(School_bus,Vehicle))
print(isinstance(School_bus,Bus))
print(issubclass(Bus,Vehicle))
