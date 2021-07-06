ncasos=int(input())
for i in range(ncasos):
    ninstrucoes=int(input())
    instrucaoaux=[]
    posicao=0
    for i in range(ninstrucoes):
        entrada=input()
        if(entrada=='LEFT'):
            posicao=posicao-1
            instrucaoaux.append(-1)
        if(entrada=="RIGHT"):
            posicao=posicao+1
            instrucaoaux.append(1)
        if ((entrada.startswith("SAME AS"))==True):
            same1=entrada.split()
            same2=int(same1[2])
            if(instrucaoaux[same2-1]==1):
                instrucaoaux.append(1)
            if(instrucaoaux[same2-1]==(-1)):
                instrucaoaux.append(-1)
            posicao=posicao+instrucaoaux[same2-1]
    print(posicao)