n = int(input("Введите n: "))
lst = list()
for i in range(n):
    lst.append(int(input()))
if n <= 0:
    print(0)
else:
    max = 0
    count = 1
    last = lst[0]
    for el in lst:
        if el > last:
            count += 1
            if count > max:
                max = count
        else:
            count = 1
        last = el
    print(max)
            
