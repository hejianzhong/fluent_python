from chracter06 import simple_demo
import functools
import time

#太牛了
@functools.lru_cache()
@simple_demo.clock
def fibonacci(n):
    return n if n < 2 else fibonacci(n-2) + fibonacci(n-1)

@simple_demo.clock
def fibonacci1(n):
    return n if n < 2 else fibonacci(n-2) + fibonacci(n-1)

if __name__ == "__main__":
    t0 = time.time()
    print("+++++++++++++++++++++++")
    print(f" {fibonacci1(30)}")
    print(f"没有缓存 耗时： {time.time() - t0}")

    t0 = time.time()
    print("+++++++++++++++++++++++")
    print(f" {fibonacci(30)}")
    print(f"有缓存耗时： {time.time() - t0}")