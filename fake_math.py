def divide(first, second):
    result = []
    if second == 0:
        result.append('Ошибка')
        return result
    else:
        result.append(first/second)
        return result
    print(*result)


