ncasos=int(input())
for elemento in range(1,ncasos+1):
    quant_pessoas,passo=input().split()
    quant_pessoas=int(quant_pessoas)
    passo=int(passo)
    morto=0
    for i in range(1,quant_pessoas+1):
        morto=((morto+passo)%i)
    morto=morto+1
    print("Case {}: {}".format(elemento,morto))
