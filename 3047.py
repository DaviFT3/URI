M= int(input())
A= int(input())
B= int(input())
if(40<=M<=110 and A!=B and A<M>B):
    X= M-(A+B)
    Y= max(A,B,X)
    print(Y)