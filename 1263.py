while True:
    try:
        entrada=input()
        iniciais=[]
        for palavra in entrada.split():
            iniciais.append(palavra[0].lower())
        alit=0
        aux=0
        for escala in range(0,len(iniciais)):
            if(escala==0):
                testar=iniciais[0]
                continue
            if(iniciais[escala]==testar and aux==0):
                alit+=1
                aux=1
            if(iniciais[escala]!=testar):
                testar=iniciais[escala]
                aux=0
        print(alit)   
    except EOFError:
        break