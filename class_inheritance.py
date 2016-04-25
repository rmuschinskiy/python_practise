__author__ = 'Sindbad the Sailor'


def is_parent(parent, child, classes):
    if parent == child:
        print("Yes")
        return True
    if parent in classes[child]:
        print("Yes")
        return True
    for el in classes[child]:
        if el == parent:
            print("Yes")
            return True
        is_parent(parent, el, classes)
    print("No")
    return False


def initialize(queries, classes):
    for q in queries:
        is_parent(q[0], q[1], classes)


def main():
    classes = {}
    queries = []
    undeclared_classes = {}
    num_classes = int(input())
    counter = 0
    while counter < num_classes:
        cls = str(input()).split(sep=":")
        child_class = cls[0].strip()
        if len(cls) == 2:
            parents_classes = cls[1].split()
            if child_class in classes:
                classes[child_class].extend(parents_classes)
            else:
                classes[child_class] = parents_classes
        else:
            classes[child_class] = []
        counter += 1
    for val in classes.values():
        for el in val:
            if el not in classes:
                undeclared_classes[el] = []
    classes.update(undeclared_classes)
    counter = 0
    num_queries = int(input())
    while counter < num_queries:
        qry = str(input()).split()
        queries.append(qry)
        counter += 1
    initialize(queries, classes)


if __name__ == '__main__':
    main()