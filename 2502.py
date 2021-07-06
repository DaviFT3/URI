while True:
    try:    
        tamcifra,ncasos=input().split()
        ncasos=int(ncasos)
        tamcifra=int(tamcifra)
        code1=input()
        code2=input()
        for j in range(ncasos):
            frase=input()
            for i in range(tamcifra):
                frase=frase.replace(code1[i].lower(),"}")
                frase=frase.replace(code1[i],"{")
                frase=frase.replace(code2[i].lower(),"$")
                frase=frase.replace(code2[i],"%")

                frase=frase.replace("}",code2[i].lower())
                frase=frase.replace("{",code2[i])
                frase=frase.replace("$",code1[i].lower())
                frase=frase.replace("%",code1[i])
            print(frase)
        print()
    except:
        break