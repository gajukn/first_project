def is_digit(el):
    try:
        float(el)
        return True
    except ValueError:
        return False

n = int(input());
sum = 0.0;
for i in range(n):
    el = input()
    if (el.lower() == 'true'):
        sum += 1
    elif (el.lower() == 'false'):
        sum += 0
    elif (is_digit(el)):
        sum += float(el)
print("Сумма равняется: ", round(sum, 4), "\nСреднее равняется: ", round(sum/n, 4))
