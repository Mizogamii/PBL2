"""/*******************************************************************************
Autor: Sayumi Mizogami Santana
Componente Curricular: Algoritmos I
Concluido em: 08/10/2023
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
******************************************************************************************/"""
score = 0
jogadasValidas = 0 


def imprimirInstrucoes():
    print("----------------------------------------")
    print("\t\t  2048")
    print("----------------------------------------")
    print("\t   INSTRUÇÕES DO JOGO")
    print("----------------------------------------")
    print(" Digite:")
    print(""" W para mover para cima
 S para mover para baixo
 A para mover para esquerda
 D para mover para direita""")
    print("----------------------------------------")
#Função para imprimir a matriz
def imprimirMatriz():
    print("+--------+--------+--------+--------+")
    for i in range(0,4):
        print(f"|        |        |        |        |")
        for j in range(0,4):
            if matriz[i][j] == 0:
                print("|        ", end="")
            elif matriz[i][j] < 9:
                print(f"|   {matriz[i][j]}    ", end="")

            elif matriz[i][j] < 99:
                print(f"|   {matriz[i][j]}   ", end="")
                
            elif matriz[i][j] < 999:
                print(f"|   {matriz[i][j]}  ", end="")
                
            else:
                print(f"|  {matriz[i][j]}  ", end="")
                
        print(f"|\n|        |        |        |        |")
        print("+--------+--------+--------+--------+")

#Função para copiar a matriz
def copiarMatriz():
    for i in range(0,4):
        for j in range(0,4):
            copiaMatriz[i][j] = matriz[i][j]

#Função para verificar se há números que podem ser somados nas colunas da matriz
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
    return contadorIguaisColuna

#Função para verificar se há números que podem ser somados nas linhas da matriz
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
    return contadorIguaisLinha
        
#Quando for inserido o D(para direita), essa função serve para inserir os números na lista e depois imprimir na matriz
def localMatrizD():
    for linha in range(0,4):
        for i in range(0,4):
            lista[i] = 0
            
        for i in range(0,4):
            lista[i] = matriz[linha][i]
        
        arrumacao2()
                    
        for i in range(0,4):
            matriz[linha][i] = lista[i]
        
#Quando for inserido o W(para descer), essa função serve para inserir os números na lista e depois imprimir na matriz        
def localMatrizS():
    for coluna in range(0,4):
        for i in range(0,4):
            lista[i] = 0
            
        for i in range(0,4):
            lista[i] = matriz[i][coluna]
            
        arrumacao2()
                    
        for i in range(0,4):
            matriz[i][coluna] = lista[i] 
               
#Quando for inserido o W(para subir), essa função serve para inserir os números na lista e depois imprimir na matriz
def localMatrizW():
    for coluna in range(0,4):
        for i in range(0,4):
            lista[i] = 0
            
        for i in range(0,4):
            lista[i] = matriz[i][coluna]

        arrumacao()
                    
        for i in range(0,4):
            matriz[i][coluna] = lista[i]
        
#Quando for inserido o A(para a esquerda), essa função serve para inserir os números na lista e depois imprimir na matriz        
def localMatrizA():
    for linha in range(0,4):
        for i in range(0,4):
            lista[i] = 0
            
        for i in range(0,4):
            lista[i] = matriz[linha][i]
            
        arrumacao()
                    
        for i in range(0,4):
            matriz[linha][i] = lista[i]
            
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

#Fazendo a matriz e as listas 
matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
copiaMatriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
lista = [0, 0, 0, 0]
listaVerificacao = [0, 0, 0, 0]
continuar = "S"

"""#Para testar todos os números diferentes           
matriz[0][0] = 2
matriz[0][1] = 4
matriz[0][2] = 6
matriz[0][3] = 8
matriz[1][0] = 10
matriz[1][1] = 12 
matriz[1][2] = 14
matriz[1][3] = 16
matriz[2][0] = 18
matriz[2][1] = 20
matriz[2][2] = 22
matriz[2][3] = 24
matriz[3][0] = 26
matriz[3][1] = 28
matriz[3][2] = 0
matriz[3][3] = 0"""

"""#Para testar números iguais
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
matriz[3][3] = 32"""

#Para continuar o loop até o usuário desejar encerrar 
while continuar != "N" and continuar != "n":
    #Inserindo os zeros na matriz
    for i in range(0,4):
        for j in range(0,4):
            matriz[i][j] = 0
         
    #Lista dos números que poderão ser sorteados 
    numeros = [2,4]
    ganhou = False
    perdeu = False
    
    #Para continuar o loop até perder ou ganhar o jogo
    while ganhou != True and perdeu != True:  
        temEspaco = False
        
        imprimirInstrucoes()
        if contador > 0:
            imprimirMatriz()
                       
        if contador == 0:
            for sorteio in range(2):
                numeroSorteado = (random.choice(numeros)) 
                
                #Sorteio da posição em que o número sorteado(2 ou 4) vai ser inserido na matriz e a inserção dele na matriz 
                linha = (random.randint(0, 3)) 
                coluna = (random.randint(0, 3)) 
                
                if matriz[linha][coluna] == 0: 
                    matriz[linha][coluna] = numeroSorteado          
                    
            imprimirMatriz()
        
        contador += 1
            
        copiarMatriz()
        
        #Verificar se tem números iguais na matriz que podem ser somados posteriormente   
        contadorIguaisColuna = verificandoIgualdadesColuna()
        contadorIguaisLinha = verificandoIgualdadesLinha()
                           
        print(f"Score: {score}")
        print(f"Jogadas válidas: {jogadasValidas}")
    
        #Para verificar se tem espaço na matriz
        for i in range(0,4):
            for j in range(0,4):
                if matriz[i][j] == 0:
                    temEspaco = True
        
        #Verificação da vitória do usuário
        for i in range(0,4):
            for j in range(0,4):
                if matriz[i][j] == 2048:
                    print("GANHOU!")
                    print("Parabéns!!!\n2048!")
                    ganhou = True
                    
        #Verificação da derrota do usuário    
        if ganhou != True:
            if temEspaco == False:
                if contadorIguaisColuna == 0 and contadorIguaisLinha == 0:
                    perdeu = True
                    print("PERDEU!")
                    break
        
        movimentos = input("Informe o comando [W, S, A, D]: ")
        movimentos = movimentos.upper()

        while movimentos != "W" and movimentos != "S" and movimentos != "A" and movimentos != "D":
            movimentos = input("Informe o comando [W, S, A, D]: ")
            movimentos = movimentos.upper()
    
        if movimentos == "W":
            localMatrizW()
            
        elif movimentos == "A":    
            localMatrizA()
            
        elif movimentos == "D": 
            localMatrizD()
            
        elif movimentos == "S": 
            localMatrizS()
                
        """
        Para testar 
        if contador == 3:
            matriz[3][3] = 2048"""
        
        #Comparação da matriz antes e depois dos movimentos para verificar se moveu
        saoDiferentes = False
        
        for i in range(0,4):
            for j in range(0,4):
                if matriz[i][j] != copiaMatriz[i][j]:
                    saoDiferentes = True
                    
        #Sorteio dos números que vão ser inseridos na matriz(podendo ser 2 ou 4) com condições de ter espaço e ter tido movimentos antes
        if contador > 0 and temEspaco == True and saoDiferentes == True: 
            numeroSorteado = (random.choice(numeros)) 
            
            #Sorteio da posição em que o número sorteado(2 ou 4) vai ser inserido na matriz e a inserção dele na matriz 
            linha = (random.randint(0, 3)) 
            coluna = (random.randint(0, 3)) 
            
            while matriz[linha][coluna] != 0:
                linha = (random.randint(0, 3)) 
                coluna = (random.randint(0, 3))
                
            matriz[linha][coluna] = numeroSorteado
        
        imprimirMatriz()
        
        print("----------------------------------------")  
        print(f"Jogadas válidas: {jogadasValidas}")     
        print('\033c', end='')


    print("----------------------------------------")
    print("            RESULTADO DO JOGO           ")   
    print("----------------------------------------") 
    print(f"Score final: {score}")
    print(f"Jogadas válidas: {jogadasValidas}") 
    print(f"Quantidade de jogadas: {contador}")
    print("----------------------------------------") 
    continuar = input("Deseja continuar jogando?[S/N]: ")
    
    #Para zerar o jogo e iniciar um novo
    if continuar != "N" and continuar != "n":
        score = 0
        jogadasValidas = 0
        contador = 0
        perdeu = False
        ganhou = False
print("Encerrando...")
    