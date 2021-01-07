iter_obj = iter([1, 2, 3])
while True:
    try:
        element = next(iter_obj)
        # ...do something with element
        print(element)
    except StopIteration:
        break

iter_obj
