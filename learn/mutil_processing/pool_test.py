from multiprocessing import Pool


def f(x, y):
    return x*y


if __name__ == '__main__':
    with Pool(5) as p:
        print(p.starmap(f, [[1, 1], [2, 2], [3, 3]]))