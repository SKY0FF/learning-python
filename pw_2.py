class Auto:

    def __init__(self, mofified):
        self.MaxSpeed = 325
        self.Name = "Lamborghini Huracan"
        self.BodyType = "Coupe"
        self.AmountOfDoors = 2
        self.SizeTruck = 100
        self.modified = mofified
    
    def get_year_of_issue(self):
        return "Год выпуска - 2014"
    
    def get_acceleration_to_one_hundred(self):
        return 3.2
    
    def get_cylinder_arrangement(self):
        return "V-образный"

car = Auto("True")
print(car.modified)
print(car.get_acceleration_to_one_hundred())
print(car.get_year_of_issue())