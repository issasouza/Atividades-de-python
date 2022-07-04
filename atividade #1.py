num = int(input())
de = int(input())
ate = int(input())

print("Tabuada do %d de %d até %d" % (num, de, ate))

for i in range(de, ate):
    print("%d X %d = %d" % (num, i, num*i))
