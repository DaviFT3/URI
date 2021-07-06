entrada=input()
saida='='
for palavras in entrada.split():
    palavras=palavras.replace('pp','+')
    palavras=palavras.replace('p','')
    saida=saida+'='+palavras
saida=saida.replace('+','p')
saida=saida.replace('=','',2)
saida=saida.replace('=',' ')
print(saida)