def manipulate(num1, num2):
    count = 0
    if num1 % num2 == 0:
        num1 = num1 - num2
        count = -1
    else:
        for i in range(4):
            num1 = num1 + num2 * i
            count = count + 1
    if count % num1 == 1:
        return True
    return False
