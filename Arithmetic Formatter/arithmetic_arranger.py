def arithmetic_arranger(problems, var=None):
    if len(problems) > 5:
        return "Error: Too many problems."

    arr1 = []
    arr2 = []
    arr3 = []
    arr4 = []

    for i in problems:
        arr = i.split()

        num1 = arr[0]
        operator = arr[1]
        num2 = arr[2]
        # check for are num1 and num2 number
        if num1.isdigit() is False or num2.isdigit() is False:
            return "Error: Numbers must only contain digits."
        # check for number length
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."
        # check for the operator
        match operator:
            case '+':
                pass
            case '-':
                pass
            case _:
                return "Error: Operator must be '+' or '-'."
        # check for the longest number to find problem size
        if len(num1) > len(num2):
            esize = len(num1) + 2
        else:
            esize = len(num2) + 2

        line1 = f'{num1}'
        line1 = line1.rjust(esize)
        arr1.append(str(line1))

        line2 = f'{operator}'
        line2 = line2.ljust(esize - len(str(num2)))
        line2 += f'{num2}'
        arr2.append(str(line2))

        line3 = ''
        line3 += line3.rjust(esize, "-")
        arr3.append(str(line3))
        # check for if we want the results
        if var is True:
            if operator == '+':
                result = int(num1) + int(num2)
            elif operator == '-':
                result = int(num1) - int(num2)
            line4 = f'{result}'
            line4 = line4.rjust(esize)
            arr4.append(str(line4))
        else:
            pass

    line1 = ''
    line2 = ''
    line3 = ''
    line4 = ''

    for i in arr1:
        line1 += i + "    "
    for i in arr2:
        line2 += i + "    "
    for i in arr3:
        line3 += i + "    "
    if var is True:
        for i in arr4:
            line4 += i + "    "

    if var is True:
        return f"{line1.rstrip()}\n{line2.rstrip()}\n{line3.rstrip()}\n{line4.rstrip()}"
    elif var is None:
        return f"{line1.rstrip()}\n{line2.rstrip()}\n{line3.rstrip()}"
