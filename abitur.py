import os

file_name = os.path.join(os.getcwd(), 'dataset_3363_4.txt')
output_file = os.path.join(os.getcwd(), 'dataset_3363_4_out.txt')
students = []
math_mark_sum = 0
phys_mark_sum = 0
ruslang_mark_sum = 0
with open(output_file, 'w') as out_file_handle:
    with open(file_name, 'r') as file_handle:
        for line in file_handle:
            student_record = list(map(str.strip, line.split(';')))
            students.append(student_record)
            student_record_avg = (int(student_record[1]) + int(student_record[2]) + int(student_record[3])) / 3
            out_file_handle.write(str(student_record_avg) + '\n')
            math_mark_sum += int(student_record[1])
            phys_mark_sum += int(student_record[2])
            ruslang_mark_sum += int(student_record[3])
            # print(student_record_avg)
    out_file_handle.write(str(math_mark_sum / len(students)) + ' ')
    out_file_handle.write(str(phys_mark_sum / len(students)) + ' ')
    out_file_handle.write(str(ruslang_mark_sum / len(students)))
