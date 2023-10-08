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

#Função verificar se há espaços na matriz
def verificacaoEspacosMatriz():
    temEspaco = False
    for i in range(0,4):
        for j in range(0,4):
            if matriz[i][j] == 0:
                temEspaco = True
    return temEspaco

#Função para sortear o número
def sorteioNumero():
    sortear = (random.randint(0,100))
    if sortear < 90: 
        numeroSorteado = 2
    else: 
        numeroSorteado = 4
    #Sorteio da posição em que o número sorteado(2 ou 4) vai ser inserido na matriz e a inserção dele na matriz 
    linha = (random.randint(0, 3)) 
    coluna = (random.randint(0, 3)) 
    
    while matriz[linha][coluna] != 0:
        linha = (random.randint(0, 3)) 
        coluna = (random.randint(0, 3))
        
    matriz[linha][coluna] = numeroSorteado
        
#Função para imprimir as intruções 
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
        
        arrumacaoDecrescente()
                    
        for i in range(0,4):
            matriz[linha][i] = lista[i]
        
#Quando for inserido o W(para descer), essa função serve para inserir os números na lista e depois imprimir na matriz        
def localMatrizS():
    for coluna in range(0,4):
        for i in range(0,4):
            lista[i] = 0
            
        for i in range(0,4):
            lista[i] = matriz[i][coluna]
            
        arrumacaoDecrescente()
                    
        for i in range(0,4):
            matriz[i][coluna] = lista[i] 
               
#Quando for inserido o W(para subir), essa função serve para inserir os números na lista e depois imprimir na matriz
def localMatrizW():
    for coluna in range(0,4):
        for i in range(0,4):
            lista[i] = 0
            
        for i in range(0,4):
            lista[i] = matriz[i][coluna]

        arrumacaoCrescente()
                    
        for i in range(0,4):
            matriz[i][coluna] = lista[i]
        
#Quando for inserido o A(para a esquerda), essa função serve para inserir os números na lista e depois imprimir na matriz        
def localMatrizA():
    for linha in range(0,4):
        for i in range(0,4):
            lista[i] = 0
            
        for i in range(0,4):
            lista[i] = matriz[linha][i]
            
        arrumacaoCrescente()
                    
        for i in range(0,4):
            matriz[linha][i] = lista[i]
            
#Serve para organizar e somar os números na lista para as opções S e D (Descer e direita)
def arrumacaoDecrescente():      
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
def arrumacaoCrescente():    
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

matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]] 
copiaMatriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
lista = [0, 0, 0, 0]
listaVerificacao = [0, 0, 0, 0]
listaScore = []
listaQuantidadeJogadas = []
listaContador = []
continuar = "S"
contador = 0

#Para continuar o loop até o usuário desejar encerrar 
while continuar != "N" and continuar != "n":
    ganhou = False
    perdeu = False
    score = 0
    jogadasValidas = 0
    contador = 0
    matrizCheia = False
    
    #Inserindo os zeros na matriz
    for i in range(0,4):
        for j in range(0,4):
            matriz[i][j] = 0
  
    #Para continuar o loop até perder ou ganhar o jogo
    while ganhou != True and perdeu != True:   
        temEspaco = False
        
        imprimirInstrucoes()
        if contador == 0:
            for sorteio in range(2): 
                sorteioNumero()  
                    
        imprimirMatriz()
        
        print(f"Score: {score}")
        
        contador += 1
            
        copiarMatriz()
     
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
       
        #Para verificar se tem espaço na matriz
        temEspaco = verificacaoEspacosMatriz()
        
        #Comparação da matriz antes e depois dos movimentos para verificar se moveu
        saoDiferentes = False
        
        for i in range(0,4):
            for j in range(0,4):
                if matriz[i][j] != copiaMatriz[i][j]:
                    saoDiferentes = True
                    
        #Sorteio dos números que vão ser inseridos na matriz(podendo ser 2 ou 4) com condições de ter espaço e ter tido movimentos antes
        if contador > 0 and temEspaco == True and saoDiferentes == True: 
            sorteioNumero()
            
        #Para verificar se tem espaço na matriz após a inserção do número sorteado
        temEspaco = verificacaoEspacosMatriz()
        
        #Verificar se tem números iguais na matriz que podem ser somados posteriormente   
        contadorIguaisColuna = verificandoIgualdadesColuna()
        contadorIguaisLinha = verificandoIgualdadesLinha()
        
        #Verificação da vitória do usuário
        for i in range(0,4):
            for j in range(0,4):
                if matriz[i][j] == 2048:
                    ganhou = True           
        
        #Verificação da derrota do usuário    
        if ganhou != True:
            if temEspaco == False:
                if contadorIguaisColuna == 0 and contadorIguaisLinha == 0:
                    perdeu = True   
    
        print("----------------------------------------")  
        print(f"Jogadas válidas: {jogadasValidas}")     
        print('\033c', end='')
    
    #Inserindo os scores e a quantidade de jogadas em uma lista para mostrar no histórico
    listaScore.append(score)
    listaQuantidadeJogadas.append(jogadasValidas)
    
    print("----------------------------------------")
    print("            RESULTADO DO JOGO           ")   
    print("----------------------------------------") 
    print(f"Score final: {score}")
    print(f"Jogadas válidas: {jogadasValidas}") 
    print(f"Quantidade de movimentos realizados: {contador}")
    print("----------------------------------------")
    
    if ganhou == True:
        imprimirMatriz()
        print("GANHOU!")
        print("Parabéns!!!\n2048!")
    elif perdeu == True:
        imprimirMatriz()
        print("PERDEU!\nTente novamente!!")
    
    mostrarHistorico = input("Deseja ver o histórico do jogo? [S/N]")
    
    if mostrarHistorico != "N" and mostrarHistorico != "n":
        print('\033c', end='')
        print("----------------------------------------")
        print("            HISTÓRICO DO JOGO           ")   
        print("----------------------------------------")
        print("Score anteriores")
        print("........................................")
        
        for elementos in listaScore:
            print(elementos, end=" ")
            
        print("\n\n........................................") 
        print("Jogadas realizadas")
        print("........................................")
        for elementos2 in listaQuantidadeJogadas: 
            print(elementos2, end=" ")
        print("\n\n----------------------------------------\n") 
        
    continuar = input("Deseja continuar jogando?[S/N]: ")
    print('\033c', end='')
        
print("Encerrando...")   