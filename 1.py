name_product = input("Введите наименование товара: ")
cena_za_kg = float(input("Введите цену за 1кг: "))
massa = float(input("Введите массу товара: "))
summa_deneg = float(input("Введите количество денег: "))
summa = cena_za_kg * massa
sdacha = summa_deneg - summa
print("Чек")
print("Товар:", name_product)
print("Цена за 1кг:", cena_za_kg,"rub")
print("Масса:", massa,"kg")
print("Ваши деньги:", summa_deneg,"rub")
print("Итого:", summa,"rub")
print("Сдача:", sdacha,"rub")
