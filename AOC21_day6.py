f=open('input.txt','r')
r=f.read()
r=r.split(',')
h=[]
for elem in r:
    h.append(int(elem))

def shi(h,i):
    r=[]
    for n in range(9):
        t=0
        l = [n]
        while t<i:
            t+=1
            for k in range(len(l)):
                if l[k]==0:
                    l[k]=6
                    l.append(8)
                else:
                    l[k]-=1
        r.append(l)
    print(len(r))
    f=[]
    a=0
    for n in range(1):
        f=[]
        print(n)
        for k in range(len(h)):
            f=f+r[h[k]]
        print(len(f))
        h=f
        del(f)
        a=len(h)
        for n in range(9):
            a+=(len(r[n])-1)*h.count(n)



    return a

print(shi(h,128))


