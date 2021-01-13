def decorate_with_asterisks(func):
    def dec():
        print("*" * 20)
        func()
        print("*" * 20)

    return dec

def decorate_with_dash(func):
    def dec():
        print("-" * 20)
        func()
        print("-" * 20)

    return dec


def decorate_with_lines(func):
    def dec():
        print("=" * 20)
        func()
        print("=" * 20)

    return dec


@decorate_with_lines
@decorate_with_asterisks
@decorate_with_dash
def some_func():
    print("i did many things...")


some_func()
