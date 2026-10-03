n = int(input())
string1 = list(map(int, input().split()))
m = int(input())
string2 = list(map(int, input().split()))
if len(string1) != n or len(string2) != m:
    print("Введено неверное количество чисел")
else:
    fin = list()
    for el in string1:
        if el not in fin:
            fin.append(el)
    for el in string2:
        if el not in fin:
            fin.append(el)
    print(" ".join(map(str,fin)))
