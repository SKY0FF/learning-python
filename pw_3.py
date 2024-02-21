class Vehicle:

    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def move(self):
        print('Это транспортное средство перемещается')

class Auto(Vehicle):

    def __init__(self, body_type):
        self.body_type = body_type

    def ride(self):
        print("Это транспортное средство ездит")

class Airplane(Vehicle):

    def __init__(self, airplane_type):
        self.type = airplane_type
        
    def fly(self):
        print("Это транспортное средство летает")
