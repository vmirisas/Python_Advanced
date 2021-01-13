def decorate_gt_zero(func):
    def dec(a, b):
        if a <= 0 or b <= 0:
            print("Error: both args must be positive!")
        else:
            func(a, b)

    return dec


@decorate_gt_zero
def some_func(a, b):
    print(a * b)


some_func(1, 4)
some_func(-1, 3)
