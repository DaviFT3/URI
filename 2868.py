casos=int(input())
for i in range(casos):
    n1,op,n2,igualdade,resp=input().split()
    n1=int(n1)
    op=str(op)
    n2=int(n2)
    igualdade=str(igualdade)
    resp=int(resp)
    if(op=='+'):
        certo=n1+n2
    elif(op=='-'):
        certo=n1-n2
    else:
        certo=n1*n2
    dif=certo-resp
    if(dif<0):
        dif=dif*(-1)
    s1="E"
    s2='ou!' 
    for i in range(dif):
        s1=s1+'r'
    s1=s1+s2
    print(s1)