def logged(func):
    def wrapper(*args, **kwargs):
        print(f"Called: {func.__name__:^10}")
        return func(*args, **kwargs)

    return wrapper


@logged
def add(x, y):
    return x + y


print(add(5, 2))
