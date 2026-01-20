a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
d = int(input("d = "))

if a <= d and c <= b:
    min_bd = b
    if min_bd > d:
        min_bd = d

    max_ac = a
    if max_ac < c:
        max_ac = c

    print(min_bd - max_ac + 1)
else:
    print("2 doan khong co giao nhau")