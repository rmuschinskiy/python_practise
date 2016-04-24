__author__ = 'Sindbad the Sailor'

# Напишите реализацию функции closest_mod_5,
# принимающую в качестве единственного аргумента целое число x и возвращающую самое маленькое целое число y, такое что:
#
# y больше или равно x
# y делится нацело на 5
# Формат того, что ожидается от вас в качестве ответа:

def closest_mod_5(x):
    if x % 5 == 0:
        return x
    mod_5 = x % 5
    print(mod_5)
    return x + 5 - mod_5


# closest_mod_5(98)
# res = closest_mod_5(98)
# print(res)

def s(a, *vs, b=10):
    res = a + b
    for v in vs:
        res += v
    return res

print(s(11, 10))

def h():
    print(12)


def f():
    g(h)


def a():
    print('inside a func')


def g(a):
    a()


# g(f)

