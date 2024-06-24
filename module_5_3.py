class Building:
    def __init__(self, numbersOfFloor, buildingType):
        self.numbersOfFloor = int(numbersOfFloor)
        self.buildingType = str(buildingType)

    def __eq__(self, other):
        return (self.numbersOfFloor == other.numbersOfFloor
                and self.buildingType == other.buildingType)

b1 = Building(12, "Здание")
b2 = Building(12, "Здание")
print(b1 == b2)