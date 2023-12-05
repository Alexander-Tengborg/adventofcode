import multiprocessing

def print_cube(num):
    aa1 = num * num * num
    return aa1


def main():
    with multiprocessing.Pool(5) as p:
        results = p.map(print_cube, range(10, 15))
    print(results)


if __name__ == "__main__":
    main()