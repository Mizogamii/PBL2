matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

matriz[0][0] = 256
matriz[0][1] = 512
matriz[0][2] = 64
matriz[0][3] = 128
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

print("+-----------------------------------+")
for i in range(0,4):
    print(f"|        |        |        |        |")
    for j in range(0,4):
        if matriz[i][j] < 9:
            if matriz[i][j] == 2:
                print("|   \033[91m{}\033[0m   ".format(matriz[i][j]), end=' ')
            elif matriz[i][j] == 4:
                print("|   \033[92m{}\033[0m   ".format(matriz[i][j]), end=' ')
            elif matriz[i][j] == 8:
                print("|   \033[93m{}\033[0m   ".format(matriz[i][j]), end=' ')
            
        elif matriz[i][j] < 99:
            if matriz[i][j] == 16:    
                print("|   \033[94m{}\033[0m  ".format(matriz[i][j]), end=' ')
            elif matriz[i][j] == 32:
                print("|   \033[95m{}\033[0m  ".format(matriz[i][j]), end=' ')
            elif matriz[i][j] == 64:
                print("|   \033[96m{}\033[0m  ".format(matriz[i][j]), end=' ')
            elif matriz[i][j] == 128:
                print("|\033[95m{}\033[0m   ".format(matriz[i][j]), end='')
            elif matriz[i][j] == 256:
                print("|\033[94m{}\033[0m   ".format(matriz[i][j]), end='')
            elif matriz[i][j] == 512:
                print("|\033[93m{}\033[0m   ".format(matriz[i][j]), end='')
            
        elif matriz[i][j] < 999:
            print(f"|   {matriz[i][j]}  ", end="")
            
        else:
            print(f"|  {matriz[i][j]}  ", end="")
            
    print(f"|\n|        |        |        |        |")
    print("+-----------------------------------+")
        
