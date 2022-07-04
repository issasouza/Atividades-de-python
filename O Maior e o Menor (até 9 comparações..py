a = int(input())
b = int(input())
c = int(input())

if a > b:
   if a > c:
        maior = a
if b > a:
    if b > c:
        maior = b
if c > a:
    if c > b:
        maior = c
if a < b:
    if a < c:
        menor = a
if b < a:
    if b < c:
        menor = b
if c < a:
    if c < b:
        menor = c

print("maior:", maior)
print("menor:", menor)
