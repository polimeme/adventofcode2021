f=open('input.txt','r')
r=f.readlines()
h=[]
for elem in r:
    h.append(str((elem)[:-1]))
h[-1]=r[-1]

def binario(a,b):
    pp=[]
    for elem in [a,b]:
        l=len(elem)
        n=0
        for k in elem:
            l-=1
            n+=pow(2,l)*int(k)
        pp.append(n)
    return pp[0]*pp[1]

def genji(h):
    gamma,epsilon='',''
    for k in range(len(h[0])):
        uno=0
        zero=0

        for elem in h:
            if elem[k]=="1":
                uno+=1
            else:
                zero+=1
        if uno>zero:
            gamma+='1'
            epsilon+='0'
        else:
            epsilon+='1'
            gamma+='0'
    return binario(epsilon,gamma)

def kumasawa(h,n):
    zero=[]
    uno=[]
    for elem in h:
        if elem[n]=='0':
            zero.append(elem)
        else:
            uno.append(elem)
    if len(zero)>len(uno):
        return zero,uno
    elif len(uno)>len(zero):
        return uno,zero
    else:
        return uno,zero

def nanjo(h):
    uno, zero = kumasawa(h, 0)
    zero2, uno2 = kumasawa(h, 0)
    for n in (range(1,len(h[0]))):
        if len(uno)!=1:
            uno,zero=kumasawa(uno,n)
        if len(uno2)!=1:
            zero2,uno2=kumasawa(uno2,n)
    return binario(uno[0],uno2[0])


print("PT1:",genji(h),"\nPT2:",nanjo(h))





