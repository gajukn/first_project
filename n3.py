import math

string = input()
i, j = map(int, input().split())
string = list(string)
if (i < 0 or j > len(string) or i > j):
    print("Индексы выходят за пределы строки")
else:
    for el in range(math.floor((j - i)/2)): 
        buff = string[i + el]
        string[i + el] = string[j - el]
        string[j - el] = buff
    print("".join(string))
