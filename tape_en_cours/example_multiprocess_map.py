from multiprocessing import Pool
import time


def f(x):
    print(x)
    time.sleep(20)
    return x * x


if __name__ == "__main__":
    with Pool(5) as p:
        print(p.map(f, range(10)))
