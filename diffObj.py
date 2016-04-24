__author__ = 'Sindbad the Sailor'



def main():
    d = {}
    for obj in objects:
        obj_id = id(obj)
        if obj_id not in d:
            d[obj_id] = [obj]
        else:
            d[obj_id].append(obj)
    print(len(d))


if __name__ == '__main__':
    main()