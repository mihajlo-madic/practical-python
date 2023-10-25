import time


def timethis(original_func):
    def wrapper_func(*args, **kwargs):
        start_time = time.time()
        original_func(*args, **kwargs)
        end_time = time.time()
        print(f"Time of execution: {end_time - start_time:>2.8f} [s]")
        return original_func

    return wrapper_func
