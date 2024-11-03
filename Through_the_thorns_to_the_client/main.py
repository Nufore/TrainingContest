x = 5
y = 10

def my_func(z):
    a = 3
    print(globals()) # выводит все глобальные переменные
    print(locals()) # выводит все локальные переменные

my_func(7)