def Maior_Substring(s1, s2):
   m = [[0] * (1 + len(s2)) for i in range(1 + len(s1))]
   maior, x_maior = 0, 0
   for x in range(1, 1 + len(s1)):
       for y in range(1, 1 + len(s2)):
           if s1[x - 1] == s2[y - 1]:
               m[x][y] = m[x - 1][y - 1] + 1
               if m[x][y] > maior:
                   maior = m[x][y]
                   x_maior = x
           else:
               m[x][y] = 0
   return s1[x_maior - maior: x_maior]
while True:
    try:
        entrada1=input()
        entrada2=input()
        resultado=Maior_Substring(entrada1,entrada2)
        tam_resultado=len(resultado)
        print(tam_resultado)
    except EOFError:
        break