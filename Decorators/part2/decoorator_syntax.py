def decorate_with_lines(func):
    def dec():
        print("=" * 20)
        func()
        print("=" * 20)

    return dec



@decorate_with_lines
def some_func():
    print("i did many things...")


some_func()
