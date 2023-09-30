score = 0
jogadasValidas = 0 

def verificandoIgualdadesColuna():
    contadorIguaisColuna = 0
    for j in range(0,4):
        for i in range(0,4):
            listaVerificacao[i] = 0
            
        for i in range(0,4):
            listaVerificacao[i] = matriz[i][j]
        
        for i in range(0,4):
            if i < 3:
                if listaVerificacao[i] == listaVerificacao[i+1] and listaVerificacao[i] != 0:
                    contadorIguaisColuna += 1
    print(f"Contador colunas: {contadorIguaisColuna}")                
    return contadorIguaisColuna

def verificandoIgualdadesLinha():
    contadorIguaisLinha = 0
    for j in range(0,4):    
        for i in range(0,4):
            listaVerificacao[i] = 0
            
        for i in range(0,4):
            listaVerificacao[i] = matriz[j][i]
        
        for i in range(0,4):
            if i < 3:
                if listaVerificacao[i] == listaVerificacao[i+1] and listaVerificacao[i] != 0:
                    contadorIguaisLinha += 1
    print(f"Contador linha: {contadorIguaisLinha}")
    return contadorIguaisLinha
        
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
listaVerificacao = [0, 0, 0, 0]
continuar = "S"

#Para testar            
matriz[0][0] = 2
matriz[0][1] = 4
matriz[0][2] = 4
matriz[0][3] = 2
matriz[1][0] = 2
matriz[1][1] = 2 
matriz[1][2] = 4
matriz[1][3] = 2
matriz[2][0] = 4
matriz[2][1] = 8
matriz[2][2] = 4
matriz[2][3] = 4
matriz[3][0] = 2
matriz[3][1] = 8
matriz[3][2] = 16
matriz[3][3] = 32 

while continuar != "N" and continuar != "n":
    #Inserindo os zeros na matriz
    """for i in range(0,4):
        for j in range(0,4):
            matriz[i][j] = 0"""
         
    #Lista dos números que poderão ser sorteados 
    numeros = [2,4]
    ganhou = False
    perdeu = False
    
    while ganhou != True and perdeu != True:  
        temEspaco = False
        matrizCheia = False
        #Para verificar se tem espaço na matriz
        """matrizCheia = all(all(element != 0 for element in sublist) for sublist in matriz)
        print(matrizCheia)"""
        for i in range(0,4):
            for j in range(0,4):
                if matriz[i][j] == 0:
                    temEspaco = True
                    #Preciso arranjar uma maneira de guardar onde é que tem espaço para quando já tiver quase tudo cheio ele ir direto no ponto em vez de ficar testando achar
        
        for i in range(0,4):
            for j in range(0,4):
                if matriz[i][j] == 2048:
                    print("Parabéns!!!\n2048!")
                    ganhou = True
                       
        print(f"Contador: {contador}")
        if contador > 0 and temEspaco == True:
            #Sorteio dos números que vão ser inseridos na matriz(podendo ser 2 ou 4)
            numeroSorteado = (random.choice(numeros)) 
            print(f"{numeroSorteado}")
            
            #Sorteio da posição em que o número sorteado(2 ou 4) vai ser inserido na matriz e a inserção dele na matriz 
            
            linha = (random.randint(0, 3)) 
            coluna = (random.randint(0, 3)) 
            print(f"Linha1: {linha}  Coluna1: {coluna}")
            
            while matriz[linha][coluna] != 0:
                linha = (random.randint(0, 3)) 
                coluna = (random.randint(0, 3))
                
            matriz[linha][coluna] = numeroSorteado
            print(f"Linha2: {linha}  Coluna2: {coluna}")
                     
        elif contador == 0:
            for sorteio in range(2):
                numeroSorteado = (random.choice(numeros)) 
                print(f"{numeroSorteado}")
                
                #Sorteio da posição em que o número sorteado(2 ou 4) vai ser inserido na matriz e a inserção dele na matriz 
                linha = (random.randint(0, 3)) 
                coluna = (random.randint(0, 3)) 
                
                if matriz[linha][coluna] == 0: #Isso aqui pode tirar depois pq no início a matriz sempre(deveria pelo menos) estar vazia
                    matriz[linha][coluna] = numeroSorteado          
                #print(f"Linha: {linha}\nColuna: {coluna}")
        contador += 1    
        
        #Verificar se tem números iguais na matriz que podem ser somados posteriomente   
        contadorIguaisColuna = verificandoIgualdadesColuna()
        contadorIguaisLinha = verificandoIgualdadesLinha()
        
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
    
        movimentos = input("Informe o comando [W, S, A, D]: ")
        movimentos = movimentos.upper()

        while movimentos != "W" and movimentos != "S" and movimentos != "A" and movimentos != "D":
            movimentos = input("Informe o comando [W, S, A, D]: ")
            movimentos = movimentos.upper()
        
        """#Para testes
        mov = ["W", "A", "S", "D"]
        movimentos = random.choice(mov)
        print(f"Contador: {contador}")
                """
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
                
        if contador == 3:
            matriz[3][3] = 2048   
            
        print("----------------------------------------")
        print(f"IgualdadeColuna: {contadorIguaisColuna}")
        print(f"IgualdadeLinha: {contadorIguaisLinha}")   
        
        print("----------------------------------------")  
        print(f"Jogadas válidas: {jogadasValidas}")     
        
            
        matrizCheia = all(all(element != 0 for element in sublist) for sublist in matriz)
        if matrizCheia == True:
            print("Matriz cheia")
        else:
            print("Matriz com espaços")
            #matrizCheia == True and 
            
        if temEspaco == False:
            if contadorIguaisColuna == 0 or contadorIguaisLinha == 0:
                perdeu = True
                print("PERDEU!")
        
        contadorIguaisColuna = 0
        contadorIguaisLinha = 0
        
        print(f"Ganhou: {ganhou}")  
        print("-------------------------------------------------------------------------------")     
             
    print("----------------------------------------")
    print("            RESULTADO DO JOGO           ")   
    print("----------------------------------------") 
    print(f"Score final: {score}")
    print(f"Jogadas válidas: {jogadasValidas}") 
    print(f"Quantidade de jogadas: {contador}")
    print("----------------------------------------") 
    continuar = input("Deseja continuar jogando?[S/N]: ")
    score = 0
    jogadasValidas = 0
    contador = 0
print("Encerrando...")
    