import itertools
from timethis import timethis


@timethis
def loop_benchmark(n):
    for i in itertools.takewhile(lambda x: x < n, itertools.count(0)):
        pass
    print(f"Counted to {i + 1}")


n = 100000000
loop_benchmark(n)
