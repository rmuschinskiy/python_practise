def modify_list(l):
    index = 0
    for element in l[:]:
        if element % 2 == 0:
            l[index] = l[index] // 2
            index += 1
        else:
            del l[index]


l = [1, 2, 3, 4, 5, 6]
print(l)
print(modify_list(l))
print(l)