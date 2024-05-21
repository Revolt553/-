grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students2 = sorted(list(students))
Dict = {}
Dict[students2[0]]=(sum(grades[0])/len(grades[0]))
Dict[students2[1]]=(sum(grades[1])/len(grades[1]))
Dict[students2[2]]=(sum(grades[2])/len(grades[2]))
Dict[students2[3]]=(sum(grades[3])/len(grades[3]))
Dict[students2[4]]=(sum(grades[4])/len(grades[4]))
print(Dict)

# вот второй вариант как я смог сделать,
# но в идеале я хотел чтоб автоматически добавились эти уравнения для всего списка
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
grades2 = [sum(grades[0])/len(grades[0]),
            sum(grades[1])/len(grades[1]),
            sum(grades[2])/len(grades[2]),
            sum(grades[3])/len(grades[3]),
            sum(grades[4])/len(grades[4])]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students2 = sorted(list(students))
Dict = {}
Dict = dict(zip(students2, grades2))
print(Dict)
