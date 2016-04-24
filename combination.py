__author__ = 'Sindbad the Sailor'


def cmb(n, k):
    if k == 0:
        return 1
    if k > n:
        return 0
    return cmb(n - 1, k) + cmb(n - 1, k - 1)

print(cmb(7, 2))
