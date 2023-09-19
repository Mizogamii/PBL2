def localMatrizW(colunaEscolhida):
    for i in range(0,4):
        lista[i] = 0
        
    for i in range(0,4):
        lista[i] = matriz[i][colunaEscolhida]
    
    print(lista)
    for i in range (0,4):
        if i < 3: 
            if lista[i] == 0:
                lista[i] = lista[i + 1]
                lista[i + 1] = 0      
                      
    for i in range(0,4):
        if i < 3:
            if lista[i] == lista[i+1]:
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
                lista[i] = lista[i] + lista[i+1] 
                lista[i + 1] = 0
                
    for i in range (0,4):
        if i < 3: 
            if lista[i] == 0:
                lista[i] = lista[i + 1]
                lista[i + 1] = 0
                
    for i in range(0,4):
        matriz[i][colunaEscolhida] = lista[i]
        
def localMatrizA(linhaEscolhida):
    for i in range(0,4):
        lista[i] = 0
        
    for i in range(0,4):
        lista[i] = matriz[linhaEscolhida][i]
        
    print(lista)
    
    for i in range (0,4):
        if i < 3: 
            if lista[i] == 0:
                lista[i] = lista[i + 1]
                lista[i + 1] = 0      
                      
    for i in range(0,4):
        if i < 3:
            if lista[i] == lista[i+1]:
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
                lista[i] = lista[i] + lista[i+1] 
                lista[i + 1] = 0
                
    for i in range (0,4):
        if i < 3: 
            if lista[i] == 0:
                lista[i] = lista[i + 1]
                lista[i + 1] = 0
                
    for i in range(0,4):
        matriz[linhaEscolhida][i] = lista[i]
        
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
    
#Aqui tem uma parte que eu só copiei e colei várias vezes um for para ficar repetindo, isso pode ser feito com o while para não ficar essa repetição ou transformando em uma função DEPOIS PENSA NISSO E RESOLVE!
if movimentos == "W":
    localMatrizW(0)
    localMatrizW(1)
    localMatrizW(2)
    localMatrizW(3)
    
elif movimentos == "A": 
    localMatrizA(0)
    localMatrizA(1)
    localMatrizA(2)
    localMatrizA(3)
    
print("----------------------------------------")    


print("+---+---+---+---+")
for i in range(0,4):
    for j in range(0,4):
        print(f"| {matriz[i][j]} ", end="")
    print("|\n+---+---+---+---+")

print(f"{movimentos}")