__author__ = 'Sindbad the Sailor'

a = float(input())
b = float(input())
oper = str(input())
if b == 0 and (oper == '/' or oper == 'div' or oper == 'mod'):
    print("Деление на 0!")
elif oper == '+':
    print(a + b)
elif oper == '-':
    print(a - b)
elif oper == '/':
    print(a / b)
elif oper == '*':
    print(a * b)
elif oper == 'mod':
    print(a%b)
elif oper == 'pow':
    print(a**b)
elif oper == 'div':
    print(a//b)


