while True:
    linha,coluna=input().split()
    if(linha=="0" and coluna=="0"):
        break
    else:
        linha=int(linha)
        coluna=int(coluna)
        aux=[]
        aux2=""
        aux3=None
        for i in range(linha):
            entrada=input()
            aux3=len(entrada)
            if aux3==coluna:
                aux.append(entrada)
        Novas_linhas,Novas_colunas=input().split()
        for j in aux:
            for k in range(int(int(Novas_linhas)/linha)):
                for l in j:
                    aux2=l*int(int(Novas_colunas)/coluna)
                    print(aux2,end="")
                print("\n",end="")
        print()
