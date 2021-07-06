casos_teste=int(input())
for ncasos in range(casos_teste):
    nestudantes=int(input()) 
    alunos=input().split()   
    presenca=input().replace("M","").split()
    porcentfreq=[]
    aux=[]
    naulas=[]
    cont=0
    reprovados=""
    for i in presenca:
        naulas.append(len(i))
        for j in i:
            if(j=="P"):
                cont+=1
        aux.append(cont)
        cont=0
    for x in range(len(naulas)):
        porcentfreq.append(float((aux[x])/(naulas[x])))
    for comb in range(len(porcentfreq)):
        if(porcentfreq[comb]< 0.75):
            reprovados=reprovados+"*"+alunos[comb]
    reprovados=reprovados.replace("*","",1)
    reprovados=reprovados.replace("*"," ")
    print(reprovados)