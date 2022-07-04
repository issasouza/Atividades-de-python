quantidade = int(input())
canditadax = 0
canditaday = 0
nulos = 0


for i in range(0, quantidade):

    votos = str(input())

    if votos == "X":
        canditadax = canditadax + 1
    if votos == "Y":
        canditaday = canditaday + 1
    if votos == "N":
        nulos = nulos + 1
    if votos == "B":
        nulos = nulos + 1

while True:

    if canditadax > canditaday:
        print("X", canditadax)
        print("Y", canditaday)
        print("Brancos e nulos:", nulos)
        print("vitoria: X")
        break
    elif canditaday > canditadax:
        print("X", canditadax)
        print("Y", canditaday)
        print("Brancos e nulos:", nulos)
        print("vitoria: Y")
        break
    elif canditaday == canditadax:
        print("X", canditadax)
        print("Y", canditaday)
        print("Brancos e nulos:", nulos)
        print("empate!")
        break
