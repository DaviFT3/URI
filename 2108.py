maior=''
while True:
    mensagem=input()
    resp=''  
    if(mensagem!='0'):
        for palavra in mensagem.split():
            resp=resp+'-'+str(len(palavra))
            if(len(palavra) >= len(maior)):
                maior=palavra
            else:
                pass
        resp=resp.replace('-','',1) 
        print(resp)
    else:
        print("\nThe biggest word: %s" % maior)
        break