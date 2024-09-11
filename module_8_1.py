def add_everything_up(a=int or float or str, b=int or float or str):
    try:
        c = a + b
        if isinstance(c, float):
            c = round(c, 3)
        return c
    except TypeError:
        c = str(a) + str(b)
        return c


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
