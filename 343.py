import os

file_name = os.path.join(os.getcwd(), 'dataset_3363_3.txt')
repetitions = {}
with open(file_name, 'r') as file_handle:
    for line in file_handle:
        for word in line.split():
            if word.lower() in repetitions:
                repetitions[word.lower()] += 1
            else:
                repetitions[word.lower()] = 1
max_number = 0
max_key = None
for key, value in repetitions.items():
    if value > max_number:
        max_number = value
        max_key = key
    elif value == max_number:
        if key < max_key:
            max_key = key
print(max_key, max_number, end=' ')