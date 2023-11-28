class Auto:

    def __init__(self, name, max_speed, body_type, amount_of_doors, size_truck, modified, year):
        self.max_speed = max_speed
        self.name = name
        self.body_type = body_type
        self.amount_of_doors = amount_of_doors
        self.size_truck = size_truck
        self.modified = modified
        self.year = year
    
    def get_year(self):
        return f"Год поставки - {self.year}"
    
    def is_modified(self):
        if self.modified:
            return "Машина модифицированна"
        else:
            return "Машина не модифицированна"

car = Auto("Lamborghini Huracan", 325, "Coupe", 2, 100, True, 2023)
print(car.max_speed)
print(car.is_modified())
print(car.get_year())