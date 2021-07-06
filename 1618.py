ncasos=int(input())
for i in range(ncasos):
    ax,ay,bx,by,cx,cy,dx,dy,rx,ry=input().split()
    eixox=[]
    eixoy=[]
    resp=[]

    ax=int(ax)
    eixox.append(ax)
    bx=int(bx)
    eixox.append(bx)
    dx=int(dx)
    eixox.append(dx)
    cx=int(cx)
    eixox.append(cx)

    ay=int(ay)
    eixoy.append(ay)
    dy=int(dy)
    eixoy.append(dy)
    by=int(by)
    eixoy.append(by)
    cy=int(cy)
    eixoy.append(cy)

    
    rx=int(rx)
    ry=int(ry)
    
    for j in range(len(eixox)):
        if((j%2)==0):
            if(rx >= eixox[j] and ry>=eixoy[j]):
                resp.append(1)
        else:
            if(rx <= eixox[j]and ry <= eixoy[j]):
                resp.append(1)
    if(sum(resp)==4):
        print("1")
    else:
        print("0")