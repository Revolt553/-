class Building:
    def __init__(self, int, str):
        self.numbersOfFloor = int
        self.buildingType = str

    def __eq__(self, other):
        return (self.numbersOfFloor == other.numbersOfFloor
                and self.buildingType == other.buildingType)

b1 = Building(12, "Здание")
b2 = Building(12, "Здание")
print(b1 == b2)