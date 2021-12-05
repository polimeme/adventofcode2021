f=(open('input.txt','r'))
r=f.readlines()
i,f=[],[]
for elem in r:
    elem=elem.replace('-','').replace('>',',').replace('\n','').replace(' ','')
    elem=elem.split(',')
    i.append([elem[0],elem[1]])
    f.append([elem[2],elem[3]])

def mode(h):
    h=sorted(h)
    a=h[0]
    n=1
    b=[]
    for elem in h[1:]:
        if elem==a:
            n+=1
        else:
            a=elem
            b.append(n)
            n=1
    b=list(reversed(b))
    n=0
    for elem in b:
        if elem>1:
            n+=1
    return n


def sci(i,f):
    h,h2=[],[]
    for n in range(len(i)):
        x1,y1,x2,y2=int(i[n][0]),int(i[n][1]),int(f[n][0]),int(f[n][1])
        if x1==x2:
            for k in range(min(y1,y2),max(y1,y2)+1):
                h.append([(x1),(k)])
                h2.append([(x1), (k)])
        elif y1==y2:
            for k in range(min(x1,x2),max(x1,x2)+1):
                h.append([(k),(y1)])
                h2.append([(k), (y1)])
        else:#PT2
            l=abs(x1-x2)
            if abs(x1-x2)==abs(y1-y2):
                h2.append([x1, y1])
                h2.append([x2, y2])
                for gg in range(l-1):
                    bb = []
                    if x1 > x2:
                        x1 -= 1
                        bb.append(x1)
                    else:
                        x1 += 1
                        bb.append(x1)
                    if y1 > y2:
                        y1 -= 1
                        bb.append(y1)
                    else:
                        y1 += 1
                        bb.append(y1)
                    h2.append(bb)

    return(mode(h),mode(h2))

pt1,pt2=(sci(i,f))[0],sci(i,f)[1]
print('PT1:',pt1,'\nPT2:',pt2)
