from math import inf
def divide(first, second):
    result = []
    if second == 0:
        result.append(inf)
        return result
    else:

        result.append(first/second)
        return result
    print(*result)