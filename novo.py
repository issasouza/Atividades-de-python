quantidade = int(input())
canditadax = 0
canditaday = 0
nulos = 0

for i in range(0, quantidade):

    votos = str(input())

    if votos == "X":
        canditadax =+1
    if votos == "Y":
        canditaday =+1
    if votos == "N":
        nulos =+1
    if votos == "B":
        nulos =+1

print("X", canditadax)
print("Y", canditaday)
print("Brancos e Nulos", nulos)
if canditadax > canditaday:
    print("vitoria: X", canditadax)
if canditaday < canditadax:
    print("vitoria: Y", canditaday)
elif canditadax == canditaday:
    print("empate!")
