f=open('ambra.txt','r')
r=f.readlines()
s=r[0]
r=r[2:]
for n in range(len(r)):
    r[n] = r[n].replace("\n", '')

def hsp70(r,c,sol):
    h=[]
    l=''
    if sol%2==0:
        l='#'
    else:
        l='.'
    for elem in r:
        h.append(elem)
    for n in range(len(h)):
        #h[n]=h[n].replace("\n",'')
        h[n]=(l*c)+h[n]+(l*c)
    h=c*[(len(h[0])*l)]+h+[(len(h[0])*l)]*c
    return h



def rep(n,k,r,c,sol):
    nr=[]
    for elem in r:
        nr.append(elem)
    nr=hsp70(nr,c,sol)

    h=''
    n=n+c
    k=k+c
    for j in range(3):
        c=[-1,0,1]
        h+=nr[n+c[j]][k-1:k+2]

    h=''.join(h)
    h=h.replace('.','0').replace('#','1')

    return int(h,2)


def tonno(s,r,c,d,sol):

    h=hsp70(r,d,sol)
    hn=[]
    for elem in h:
        hn.append(list(elem))

    for n in range(len(h)):
        for k in range(len(h[n])):
            x=rep(n,k,h,c,sol)
            if s[x]=='#':
                hn[n][k]='#'
            else:
                if hn[n][k]=='#':
                    hn[n][k]='.'
    return hn

def rotate(h):
    a = h
    hn = []
    status=0
    if len(h) > len(h[0]):
        status = 1
        for n in range(len(h)):
            h[n] += ' ' * (len(h) - len(h[-1]))
    else:
        status = 2
        for n in range(len(h[0]) - len(h)):
            h.append(' ' * (len(h[0])))

    for n in range(len(a)):
        s = ''
        for k in range(len(a[n])):
            s += a[k][n]
        hn.append(s)
    if status == 1:
        while ' ' * len(h[0]) in hn:
            hn.remove(' ' * len(h[0]))

    elif status == 2:
        for n in range(len(hn)):
            hn[n] = list(hn[n])
            while ' ' in hn[n]:
                hn[n].remove(' ')
            hn[n] = ''.join(hn[n])
    return hn

def ottimizza(h):
    for n in range(int(len(h)/2)):
        if n<len(h)-3:
            if  h[n+1]==h[n] and h[n+2]==h[n]: #h[n]=='#'*len(h[n]) and
                #print(n,len(h))
                h[n]='x'
                h[len(h)-(n)-1]='x'
    while 'x' in h:
        h.remove('x')
    return h




hn=tonno(s,r,7,1,1)
for n in range(len(hn)):
    hn[n]=''.join(hn[n])

tr=49
while tr>0:

    tr-=1
    hn = tonno(s, hn, 2,4,tr)
    print(tr, len(hn), len(hn[0]))
    for n in range(len(hn)):
        hn[n]=''.join(hn[n])
    for jj in range(5):
        hn = rotate(ottimizza(rotate(hn)))
        hn=ottimizza(hn)



y=0
for elem in hn:
    y += elem.count('#')
print(y, 'bnbnbnbnbnbn')


###IL TRUCCO ERA TRASFORMARE TUTTI GLI INFINITI IN PUNTI QUANDO è DISPARI, IN ### QUANDO PARI

