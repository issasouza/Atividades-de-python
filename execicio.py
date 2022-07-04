a = int(input())
b = int(input())
c = int(input())
d = int(input())

old = a

if b > a and b > c and b > d:
    old = b
if c > a and c > b and c > d:
    old = c
if d > a and d > b and d > c:
    old = d
print("A mais velha %d tem anos" % old)
