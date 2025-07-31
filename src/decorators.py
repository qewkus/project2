from datetime import datetime
from functools import wraps
from typing import Any, Callable


def log(filename: str = "") -> Callable:
    def inner(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            start_time = datetime.now()
            try:
                result = func(*args, **kwargs)
                stop_time = datetime.now()
                if filename:
                    with open(filename, mode="a", encoding="utf-8") as f:
                        f.write(f"{start_time}, {stop_time}, {func.__name__} ok\n")
                else:
                    print(f"{start_time}, {stop_time}, {func.__name__} ok\n")
            except Exception as err:
                stop_time = datetime.now()
                with open(filename, mode="a", encoding="utf-8") as f:
                    f.write(f"{start_time}, {stop_time}, {func.__name__} error: '{err}'. Inputs: {args}, {kwargs}\n")
                raise err
            return result

        return wrapper

    return inner


@log(filename="mylog.txt")
def my_function(x: int, y: int) -> int:
    return x + y


print(my_function(1, 2))
# print(my_function(1, "b"))


@log()
def my_function_1(x: int, y: int) -> int:
    return x * y


print(my_function_1(2, 2))
