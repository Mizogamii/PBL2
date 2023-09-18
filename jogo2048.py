import random
contador = 0
j = 0
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

#Fazendo a matriz e as listas 
matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
lista = [0, 0, 0, 0]
listaExtra = [0, 0, 0, 0]

#Inserindo os zeros na matriz
for i in range(0,4):
    for j in range(0,4):
        matriz[i][j] = 0
        
#Lista dos núemros que poderão ser sorteados 
numeros = [2,4]
#Aqui botei 16 por teste mas preciso que no início seja sorteado 2 números e após isso somente 1 até a pessoa ganhar ou perder 
while contador < 16:
    score = 0
    contador += 1
    #Sorteio dos números que vão ser inseridos na matriz(podendo ser 2 ou 4)
    numeroSorteado = (random.choice(numeros)) 
    print(f"{numeroSorteado}")
    
    #Sorteio da posição em que o número sorteado(2 ou 4) vai ser inserido na matriz e a inserção dele na matriz 
    linha = (random.randint(0, 3)) 
    coluna = (random.randint(0, 3)) 
    if matriz[linha][coluna] == 0:
        matriz[linha][coluna] = numeroSorteado

    print("+---+---+---+---+")
    for i in range(0,4):
        for j in range(0,4):
            print(f"| {matriz[i][j]} ", end="")
        print("|\n+---+---+---+---+")
        
#Tá contando certo todos os números que aparecem na matriz mas só tá fazendo a conta depois de sair do loop e o score deveria aparecer a cada vez que o usuário jogar
    for i in range(0,4):
        for j in range(0,4):
            score += matriz[i][j]
    print(f"Score: {score}")
    #print('\033c', end='') Para limpar tela
 
movimentos = input("Informe o comando [W, S, A, D]: ")
movimentos = movimentos.upper()

while movimentos != "W" and movimentos != "S" and movimentos != "A" and movimentos != "D":
    movimentos = input("Informe o comando [W, S, A, D]: ")
    movimentos = movimentos.upper()
    

if movimentos == "W":
    for i in range(0,4):
        lista[i] = matriz[i][0]
        print(f"Lista: {lista}")  
        """if i < 3:    
            if lista[i] == 0:
                print("Tá igual a 0")
                lista[i] = lista[i + 1]
                lista[i + 1] = 0"""
                
    for i in range (0,4):
        if i < 3: 
            if lista[i] == 0:
                lista[i] = lista[i + 1]
                lista[i + 1] = 0      
                      
    for i in range(0,4):
        if i < 3:
            if lista[i] == lista[i+1]:
                print("Tá igual")
                lista[i] = lista[i] + lista[i+1] 
                lista[i + 1] = 0
                
    for i in range (0,4):
        if i < 3: 
            if lista[i] == 0:
                lista[i] = lista[i + 1]
                lista[i + 1] = 0
    
    for i in range(0,4):
        if i < 3:
            if lista[i] == lista[i+1]:
                print("Tá igual")
                lista[i] = lista[i] + lista[i+1] 
                lista[i + 1] = 0
                
    for i in range (0,4):
        if i < 3: 
            if lista[i] == 0:
                lista[i] = lista[i + 1]
                lista[i + 1] = 0
        #print(f"\nLista Extra: {listaExtra}")
print("----------------------------------------")    

print(lista, end=" ")
print()
#print(listaExtra, end=" ")
print(f"{movimentos}")