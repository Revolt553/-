class House:
    def __init__(self, name, numbers_of_floor):
        self.name = name
        self.numbers_of_floor = numbers_of_floor

    def go_to(self, new_floor):
        self.new_floor = int(new_floor)
        x = new_floor
        if new_floor <= self.numbers_of_floor:
            for i in range(x):
                print(i+1)
        else:
            print(f'Такого этажа не существует')

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)