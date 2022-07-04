a = int(input())
b = int(input())
c = int(input())

maior = a

if b > a and b > c:
    maior = b
elif c > a and c > b:
    maior = c
print("maior:", maior)
