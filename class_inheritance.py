__author__ = 'Sindbad the Sailor'


def is_parent(parent, child, classes):
    if len(classes[child]) == 0:
        print("No")
        return False
    for el in classes[child]:
        if el == parent:
            print("Yes")
            return True
        return is_parent(parent, el, classes)


def initialize(queries, classes):
    for q in queries:
        is_parent(q[0], q[1], classes)


def main():
    classes = {}
    queries = []
    num_classes = int(input())
    counter = 0
    while counter < num_classes:
        cls = str(input()).split(sep=":")
        child_class = cls[0].strip()
        if len(cls) == 2:
            parents_classes = cls[1].split()
            classes[child_class] = parents_classes
        else:
            classes[child_class] = []
        counter += 1
    counter = 0
    num_queries = int(input())
    while counter < num_queries:
        qry = str(input()).split()
        queries.append(qry)
        counter += 1
    initialize(queries, classes)


if __name__ == '__main__':
    main()