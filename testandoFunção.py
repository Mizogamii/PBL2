#Quando for inserido o D(para direita), essa função serve para inserir os números na lista e depois imprimir na matriz
def localMatrizD(linhaEscolhida):
    for i in range(0,4):
        lista[i] = 0
        
    for i in range(0,4):
        lista[i] = matriz[linhaEscolhida][i]
        
    print(lista)
    
    arrumacao2()
                
    for i in range(3,-1,-1):
        matriz[linhaEscolhida][i] = lista[i]
#Quando for inserido o W(para descer), essa função serve para inserir os números na lista e depois imprimir na matriz        
def localMatrizS(colunaEscolhida):
    for i in range(0,4):
        lista[i] = 0
        
    for i in range(0,4):
        lista[i] = matriz[i][colunaEscolhida]
    
    print(lista)
    
    arrumacao2()
                
    for i in range(0,4):
        matriz[i][colunaEscolhida] = lista[i]
        
#Serve para organizar e somar os números na lista para as opções S e D (Descer e direita)
def arrumacao2():
    for i in range (3,-1,-1):
        if i > 0: 
            if lista[i] == 0:
                lista[i] = lista[i - 1]
                lista[i - 1] = 0      
                      
    for i in range(3,-1,-1):
        if i > 0:
            if lista[i] == lista[i - 1]:
                lista[i] = lista[i] + lista[i - 1] 
                lista[i - 1] = 0
                
    
    for i in range (3,-1,-1):
        if i > 0: 
            if lista[i] == 0:
                lista[i] = lista[i - 1]
                lista[i - 1] = 0
                
    for i in range (3,-1,-1):
        if i > 0: 
            if lista[i] == 0:
                lista[i] = lista[i - 1]
                lista[i - 1] = 0
                
#Serve para organizar e somar os números na lista para as opções W e A (Subir e esquerda)
def arrumacao():
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
                
    for i in range (0,4):
        if i < 3: 
            if lista[i] == 0:
                lista[i] = lista[i + 1]
                lista[i + 1] = 0
                
#Quando for inserido o W(para subir), essa função serve para inserir os números na lista e depois imprimir na matriz
def localMatrizW(colunaEscolhida):
    for i in range(0,4):
        lista[i] = 0
        
    for i in range(0,4):
        lista[i] = matriz[i][colunaEscolhida]
    
    print(lista)
    
    arrumacao()
                
    for i in range(0,4):
        matriz[i][colunaEscolhida] = lista[i]
#Quando for inserido o A(para a esquerda), essa função serve para inserir os números na lista e depois imprimir na matriz        
def localMatrizA(linhaEscolhida):
    for i in range(0,4):
        lista[i] = 0
        
    for i in range(0,4):
        lista[i] = matriz[linhaEscolhida][i]
        
    print(lista)
    
    arrumacao()
                
    for i in range(0,4):
        matriz[linhaEscolhida][i] = lista[i]

#Preciso fazer o score direito e guardar para mostrar os recordes
#Reorganizar a parte de arrumação da matriz que tem parte que tá repetindo vários fors iguais
#Queria ver se consigo organizar quando o número é com dois dígitos pq tá ficando desarrumado
         
import random
contador = 0
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
continuar = "S"

while continuar != "N":
    #Inserindo os zeros na matriz
    for i in range(0,4):
        for j in range(0,4):
            matriz[i][j] = 0
            
    #Lista dos números que poderão ser sorteados 
    numeros = [2,4]
    ganhou = False

    #Aqui botei 16 por teste mas preciso que no início seja sorteado 2 números e após isso somente 1 até a pessoa ganhar ou perder 
    while matriz[i] != 0 and ganhou != True:  
        score = 0
        contador += 1
        
        if contador > 1:
            #Sorteio da posição em que o número sorteado(2 ou 4) vai ser inserido na matriz e a inserção dele na matriz 
            linha = (random.randint(0, 3)) 
            coluna = (random.randint(0, 3)) 
            if matriz[linha][coluna] == 0:
                matriz[linha][coluna] = numeroSorteado
            #Sorteio dos números que vão ser inseridos na matriz(podendo ser 2 ou 4)
            numeroSorteado = (random.choice(numeros)) 
            print(f"{numeroSorteado}")
            
        else:
            for sorteio in range(0,2):
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
    
        """movimentos = input("Informe o comando [W, S, A, D]: ")
        movimentos = movimentos.upper()

        while movimentos != "W" and movimentos != "S" and movimentos != "A" and movimentos != "D":
            movimentos = input("Informe o comando [W, S, A, D]: ")
            movimentos = movimentos.upper()"""
            
        #Para testes
        mov = ["W", "A", "S", "D"]
        movimentos = random.choice(mov)
        print(f"Contador: {contador}")
        
        if contador == 10:
            for i in range(0,4):
                matriz[0][3] = 2048
        
        for i in range(0,4):
            for j in range(0,4):
                if matriz[i][j] == 2048:
                    print("Parabéns!!!\n2048!")
                    ganhou = True
                
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
            
        elif movimentos == "D": 
            localMatrizD(0)
            localMatrizD(1)
            localMatrizD(2)
            localMatrizD(3)
            
        elif movimentos == "S": 
            localMatrizS(0)
            localMatrizS(1)
            localMatrizS(2)
            localMatrizS(3)
        print("----------------------------------------")  

        print("+---+---+---+---+")
        for i in range(0,4):
            for j in range(0,4):
                print(f"| {matriz[i][j]} ", end="")
            print("|\n+---+---+---+---+")

        print(f"{movimentos}")
    continuar = input("Deseja continuar jogando?")