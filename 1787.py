def pot2(num):
    return (num and(not(num&(num-1)))) 
def descobrir_vencedor(pontuacao_ui,pontuacao_ri,pontuacao_in):
    maior=max(pontuacao_ui,pontuacao_ri,pontuacao_in)
    if(maior==pontuacao_ui):
        if(maior==pontuacao_in or maior==pontuacao_ri):
            return("URI")
        return("Uilton")
    if(maior==pontuacao_ri):
        if(maior==pontuacao_ui or maior==pontuacao_in):
            return("URI")
        return("Rita")
    if(maior==pontuacao_in):
        if(maior==pontuacao_ui or maior==pontuacao_ri):
            return("URI")
        return("Ingred")
while True:
    nrodadas=int(input())
    if(nrodadas==0):
        break
    pontos_ui=0
    pontos_ri=0
    pontos_in=0
    for i in range(nrodadas):
        np=[]
        uilton,rita,ingred=input().split()
        uilton=int(uilton) 
        rita=int(rita)
        ingred=int(ingred)
        np.append(uilton)
        np.append(rita)
        np.append(ingred)
        if((pot2(np[0])==True)):
            pontos_ui+=1
            if((max(np))==uilton):
                pontos_ui+=1
        if((pot2(np[1])==True)):
            pontos_ri+=1
            if((max(np))==rita):
                pontos_ri+=1
        if((pot2(np[2])==True)):
            pontos_in+=1
            if((max(np))==ingred):
                pontos_in+=1    
    vencedor=descobrir_vencedor(pontos_ui,pontos_ri,pontos_in)
    print(vencedor)