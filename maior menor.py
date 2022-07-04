a = int(input())
b = int(input())

maior = 0
menor = 0

if a > b:
    maior = a
elif b > a:
    maior = b
if a < b:
    menor = a
elif b < a:
    menor = b

print("maior:", maior)
print("menor:", menor)
