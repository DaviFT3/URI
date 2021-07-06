entradas_notas=input()
entradas_notas=entradas_notas.replace("10","x")
aux=[]
for i in entradas_notas:
    if(i=="x"):
        aux.append(10)
    else:
        aux.append(int(i))
media=sum(aux)/len(aux)
print("{:.2f}".format(media))