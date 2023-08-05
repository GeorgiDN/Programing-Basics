N1 = int(input())
N2 = int(input())
operatorr = input()
result = 0
kind = ''

if operatorr == '+':
    result = N1 + N2
    if result % 2 == 0:
        kind = 'even'
    elif result % 2 != 0:
        kind = 'odd'
elif operatorr == '-':
    result = N1 - N2
    if result % 2 == 0:
        kind = 'even'
    elif result % 2 != 0:
        kind = 'odd'
elif operatorr == '*':
    result = N1 * N2
    if result % 2 == 0:
        kind = 'even'
    elif result % 2 != 0:
        kind = 'odd'
elif operatorr == '/':
    if N2 == 0:
        print(f"Cannot divide {N1} by zero")
    else:
        result = N1 / N2
elif operatorr == '%':
    if N2 == 0:
        print(f"Cannot divide {N1} by zero")
    else:
        result = N1 % N2

if operatorr == '+' or operatorr == '-' or operatorr == '*':
    print(f"{N1} {operatorr} {N2} = {result} - {kind}")
elif operatorr == '/' and N2 != 0:
    print(f"{N1} / {N2} = {result:.2f}")
elif operatorr == '%' and N2 != 0:
    print(f"{N1} % {N2} = {result}")
