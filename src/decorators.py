# Напишите декоратор log, который будет автоматически логировать начало и конец выполнения функции, а также ее результаты или возникшие ошибки.
# Декоратор должен принимать необязательный аргумент
# filename, который определяет, куда будут записываться логи (в файл или в консоль):
# Если filename задан, логи записываются в указанный файл.
# Если filename не задан, логи выводятся в консоль.

from functools import wraps
from datetime import datetime


def log(filename=""):
    def inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = datetime.now()
            try:
                result = func(*args, **kwargs)
                stop_time = datetime.now()
                if filename:
                    with open(filename, mode='a', encoding='utf-8') as f:
                        f.write(f"{start_time}, {stop_time}, {func.__name__} ok\n")
                else:
                    print(f"{start_time}, {stop_time}, {func.__name__} ok\n")
            except Exception as err:
                stop_time = datetime.now()
                with open(filename, mode='a', encoding='utf-8') as f:
                    f.write(f"{start_time}, {stop_time}, {func.__name__} error: '{err}'. Inputs: {args}, {kwargs}\n")
                raise err
            return result
        return wrapper
    return inner


@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

print(my_function(1, 2))
print(my_function(1, "b"))

@log()
def my_function_1(x, y):
    return x * y

print(my_function_1(2, 2))



