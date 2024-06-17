a = str(123)
def test_function(a):
    x = a
    def inner_function(a):
        x = 'Я в области видимости функции test_function'
        print(x)
    inner_function(a)
print(test_function(a))