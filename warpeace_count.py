string = input().split()
d = {}
for word in string:
    if word.lower() not in d:
        d[word.lower()] = 1
    else:
        d[word.lower()] = d[word.lower()] + 1
for key, value in d.items():
     print(key, value)