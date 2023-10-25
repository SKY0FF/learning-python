class Auto:

    def __init__(self, Name, MaxSpeed, BodyType, AmountOfDoors, SizeTruck, modified, year):
        self.MaxSpeed = MaxSpeed
        self.Name = Name
        self.BodyType = BodyType
        self.AmountOfDoors = AmountOfDoors
        self.SizeTruck = SizeTruck
        self.modified = modified
        self.year = year
    
    def get_year(self):
        return "Год поставки - " + str(self.year)
    
    def get_mod(self):
        if self.modified == "Yes":
            return "Машина модифицированна"
        elif self.modified == "No":
            return "Машина не модифицированна"

car = Auto("Lamborghini Huracan", 325, "Coupe", 2, 100, "Yes", 2023)
print(car.MaxSpeed)
print(car.get_mod())
print(car.get_year())