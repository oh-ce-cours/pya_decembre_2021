from multiprocessing import Pool
import time, os


def f(x):
    print(x)
    print(os.getppid(), os.getpid())
    time.sleep(20)
    return x * x


if __name__ == "__main__":
    with Pool(500000) as p:
        print(p.map(f, range(10)))
