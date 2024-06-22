class House:
    def __init__(self):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        return self.numberOfFloors

floor = House()
floor.setNewNumberOfFloors(5)
print(floor.numberOfFloors)