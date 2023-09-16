import random

print("----------------------------------------------------------------------")
print("\t\t\t\t2048")
print("----------------------------------------------------------------------")
print("INSTRUÇÕES DO JOGO")
print("----------------------------------------------------------------------")
print("Digite:")
print("""W para mover para cima
S para mover para baixo
A para mover para esquerda
D para mover para direita""")
print("----------------------------------------------------------------------")

matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

for i in range(0,4):
    for j in range(0,4):
        matriz[i][j] = 0

numeros = [2,4]

numeroSorteado = (random.choice(numeros))
print(f"{numeroSorteado}")

linha = (random.randint(0, 3)) 
coluna = (random.randint(0, 3)) 

if matriz[linha][coluna] != " ":
    matriz[i][j] = numeroSorteado

print("+---+---+---+---+")
for i in range(0,4):
    for j in range(0,4):
       print(f"| {matriz[i][j]} ", end="")
    print("|\n+---+---+---+---+")

movimentos = input("Informe o comando [W, S, A, D]: ")
movimentos = movimentos.upper()

while movimentos != "W" and movimentos != "S" and movimentos != "A" and movimentos != "D":
    movimentos = input("Informe o comando [W, S, A, D]: ")
    movimentos = movimentos.upper()

print(f"{movimentos}")