x=int(input())

def formula1(x):
    f1=(x*(x-1))/2
    return f1

def formula2(x):
    f2=x*(x-1)*(x-2)*(x-3)/(4*3*2*1)
    return f2

resposta=1+(formula1(x))+(formula2(x))
print(int(resposta))