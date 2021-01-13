def decorate_int_notzero(func):
    def dec(*args):
        for arg in args:
            if not isinstance(arg, int) or arg == 0:
                print("Error")
                return None
        func(*args)
    return dec


@decorate_int_notzero
def sum_calc(a, b):
    print(a * b)


@decorate_int_notzero
def sum_calc1(a, b, c):
    print(a * b * c)


sum_calc(3, 1)
sum_calc1(3, 2, 4)
