import functools
import time


def clock(func):
    @functools.wraps(func)
    def clocked(*args):
        t0 = time.perf_counter()
        res = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ", ".join(repr(arg) for arg in args)
        print(f"[{elapsed:0.8f}s] {name}{arg_str} -> {res!r}")
        return res
    return clocked


@clock
def snnoze(seconds:int):
    time.sleep(seconds)

@clock
def factorial(n:int) -> int:
    return 1 if n < 2 else n * factorial(n-1)

if __name__ == "__main__":
    print("+++++++++++++++++++++++")
    snnoze(.123)

    print("+++++++++++++++++++++++")
    print(f"6! = {factorial(6)}")

