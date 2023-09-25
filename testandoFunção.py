score = 0
jogadasValidas = 0 
#Quando for inserido o D(para direita), essa função serve para inserir os números na lista e depois imprimir na matriz
def localMatrizD(linhaEscolhida):
    for i in range(0,4):
        lista[i] = 0
        
    for i in range(0,4):
        lista[i] = matriz[linhaEscolhida][i]
    
    arrumacao2()
                
    for i in range(0,4):
        matriz[linhaEscolhida][i] = lista[i]
#Quando for inserido o W(para descer), essa função serve para inserir os números na lista e depois imprimir na matriz        
def localMatrizS(colunaEscolhida):
    for i in range(0,4):
        lista[i] = 0
        
    for i in range(0,4):
        lista[i] = matriz[i][colunaEscolhida]
        
    arrumacao2()
                
    for i in range(0,4):
        matriz[i][colunaEscolhida] = lista[i]        
#Quando for inserido o W(para subir), essa função serve para inserir os números na lista e depois imprimir na matriz
def localMatrizW(colunaEscolhida):
    for i in range(0,4):
        lista[i] = 0
        
    for i in range(0,4):
        lista[i] = matriz[i][colunaEscolhida]

    arrumacao()
                
    for i in range(0,4):
        matriz[i][colunaEscolhida] = lista[i]
#Quando for inserido o A(para a esquerda), essa função serve para inserir os números na lista e depois imprimir na matriz        
def localMatrizA(linhaEscolhida):
    for i in range(0,4):
        lista[i] = 0
        
    for i in range(0,4):
        lista[i] = matriz[linhaEscolhida][i]
        
    arrumacao()
                
    for i in range(0,4):
        matriz[linhaEscolhida][i] = lista[i]
#Serve para organizar e somar os números na lista para as opções S e D (Descer e direita)
def arrumacao2():      
    global score 
    global jogadasValidas
    
    for i in range(2):            
        for i in range (3,-1,-1):
            if i > 0: 
                if lista[i] == 0:
                    lista[i] = lista[i - 1]
                    lista[i - 1] = 0 
                    
    for i in range(3,-1,-1):
        if i > 0:
            contou = False 
            if lista[i] == lista[i - 1]:
                lista[i] = lista[i] + lista[i - 1] 
                lista[i - 1] = 0
                
                if lista[i] != 0:
                    contou = True
                    
                if contou == True:
                    score += lista[i]
                    jogadasValidas += 1

    for i in range(2):            
        for i in range (3,-1,-1):
            if i > 0: 
                if lista[i] == 0:
                    lista[i] = lista[i - 1]
                    lista[i - 1] = 0               
#Serve para organizar e somar os números na lista para as opções W e A (Subir e esquerda)
def arrumacao():    
    global score   
    global jogadasValidas      
     
    for i in range(2):             
        for i in range (0,4):
            if i < 3: 
                if lista[i] == 0:
                    lista[i] = lista[i + 1]
                    lista[i + 1] = 0
    
    for i in range(0,4):
        if i < 3:
            contou = False
            if lista[i] == lista[i+1]:
                lista[i] = lista[i] + lista[i+1] 
                lista[i + 1] = 0
                
                if lista[i] != 0:                
                    contou = True
                    
                if contou == True:
                    score += lista[i]
                    jogadasValidas += 1
        
    for i in range(2):             
        for i in range (0,4):
            if i < 3: 
                if lista[i] == 0:
                    lista[i] = lista[i + 1]
                    lista[i + 1] = 0         
    
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

while continuar != "N" or continuar != "n":
    #Inserindo os zeros na matriz
    for i in range(0,4):
        for j in range(0,4):
            matriz[i][j] = 0
            
    #Lista dos números que poderão ser sorteados 
    numeros = [2,4]
    ganhou = False
    #matriz[i] != 0 and ganhou != True and 
    while contador <= 100:  
        print(f"Contador: {contador}")
        if contador > 0:
            #Sorteio dos números que vão ser inseridos na matriz(podendo ser 2 ou 4)
            numeroSorteado = (random.choice(numeros)) 
            print(f"{numeroSorteado}")
            
            #Sorteio da posição em que o número sorteado(2 ou 4) vai ser inserido na matriz e a inserção dele na matriz 
            linha = (random.randint(0, 3)) 
            coluna = (random.randint(0, 3)) 
            
            while matriz[linha][coluna] != 0:
                linha = (random.randint(0, 3)) 
                coluna = (random.randint(0, 3))
                
            matriz[linha][coluna] = numeroSorteado
                     
        elif contador == 0:
            for sorteio in range(2):
                numeroSorteado = (random.choice(numeros)) 
                print(f"{numeroSorteado}")
                
                #Sorteio da posição em que o número sorteado(2 ou 4) vai ser inserido na matriz e a inserção dele na matriz 
                linha = (random.randint(0, 3)) 
                coluna = (random.randint(0, 3)) 
                
                if matriz[linha][coluna] == 0:
                    matriz[linha][coluna] = numeroSorteado          
                    
        contador += 1           
                                    
        print("+-----------------------------------+")
        for i in range(0,4):
            print(f"|        |        |        |        |")
            for j in range(0,4):
                if matriz[i][j] < 9:
                    print(f"|   {matriz[i][j]}    ", end="")

                elif matriz[i][j] < 99:
                    print(f"|   {matriz[i][j]}   ", end="")
                    
                elif matriz[i][j] < 999:
                    print(f"|   {matriz[i][j]}  ", end="")
                    
                else:
                    print(f"|  {matriz[i][j]}  ", end="")
                    
            print(f"|\n|        |        |        |        |")
            print("+-----------------------------------+")
                    
        print(f"Score: {score}")
        print(f"Jogadas válidas: {jogadasValidas}")
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
                
        #Aqui tem uma parte que eu só copiei e colei várias vezes um for para ficar repetindo, isso pode ser feito com o while para não ficar essa repetição ou transformando em uma função DEPOIS PENSA NISSO E RESOLVE!
        if movimentos == "W":
            for i in range(0,4):    
                localMatrizW(i)
            
        elif movimentos == "A": 
            for i in range(0,4):     
                localMatrizA(i)
            
        elif movimentos == "D": 
            for i in range(0,4):     
                localMatrizD(i)
            
        elif movimentos == "S": 
            for i in range(0,4): 
                localMatrizS(i)
           
        print("----------------------------------------")  
        print(f"Jogadas válidas: {jogadasValidas}")     
        """print("+---+---+---+---+")
        for i in range(0,4):
            for j in range(0,4):
                print(f"| {matriz[i][j]} ", end="")
            print("|\n+---+---+---+---+")"""
        
        for i in range(0,4):
            for j in range(0,4):
                if matriz[i][j] == 2048:
                    print("Parabéns!!!\n2048!")
                    ganhou = True
        print(f"Ganhou: {ganhou}")            
    print("----------------------------------------")
    print("            RESULTADO DO JOGO           ")   
    print("----------------------------------------") 
    print(f"Score final: {score}")
    print(f"Jogadas válidas: {jogadasValidas}") 
    print("----------------------------------------") 
    continuar = input("Deseja continuar jogando?[S/N]: ")
    score = 0
    jogadasValidas = 0
    contador = 0
    