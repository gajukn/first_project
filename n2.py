def format_name(last, first, middle=None):
    if middle == None:
        return last + " " + first
    else:
        return last + " " + first[0] + "." + middle[0] + "."

lst = list()
m = int(input())
for i in range(m):
    name = input()
    name = list(name.split())
    if len(name) < 3:
        lst.append(format_name(name[0], name[1]))
    else:
        lst.append(format_name(name[0], name[1], name[2]))
print()
for el in lst:
    print(el)
