class Buiding:
    total = 0
    def __init__(self):
        Buiding.total += 1

for i in range(40):
    b1 = Buiding()
    print(b1.total)
