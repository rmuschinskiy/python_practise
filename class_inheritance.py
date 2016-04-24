__author__ = 'Sindbad the Sailor'


def main():
    global classes
    classes = {}
    global queries
    queries = []
    num_classes = int(input())
    counter = 0
    while counter < num_classes:
        cls = str(input()).split(sep=":")
        child_class = cls[0].strip()
        if len(cls) == 2:
            parents_classes = cls[1].split()
            classes[child_class] = parents_classes
            #print(cls)
            #print(child_class)
            #print(parents_classes)
        else:
            #print(child_class)
            classes[child_class] = []
        #print(classes)
        counter += 1
    print(classes)
    counter = 0
    num_queries = int(input())
    while counter < num_queries:
        qry = str(input()).split()
        queries.append(qry)
        counter += 1
    print(queries)




if __name__ == '__main__':
    main()