f=open('input.txt','r')
r=f.readlines()
h=[]
f=[]
for elem in r:
    elem=elem.split('|')
    f.append(elem[0].split())
    h.append(elem[1].split())
l=[]
for n in range(len(h)):
    l.append([f[n],h[n]])

def oliver(h):
        p=0
        a={2:1,4:4,3:7,7:8}
        d={}
        for sub in h:
            if len(sub) in [2,4,3,7]:
                d[a[len(sub)]]=sub
                p+=1
        return p,d

def output(l,d):
    g=''
    for elem in l:
        #print(elem)
        for n in range(10):
            if sorted(dict.fromkeys(list(elem)+list(d[n])))==sorted(list(d[n])) and sorted(dict.fromkeys(list(elem)+list(d[n])))==sorted(list(elem)):
                #print(elem,d[n])
                g+=str(n)
    return g


def maddogwayne(l):
    f=0
    gg=0
    for elem in l:
        gg+=oliver(elem[1])[0]
        d=oliver(elem[0])[1]
        for parola in elem[0]:
            if len(parola)==6:
                nine=0
                for lettera in d[4]:
                    if lettera in parola:
                        nine+=1
                if nine==len(d[4]):
                    d[9]=parola
                else:
                    if len(list(dict.fromkeys(list(parola)+list(d[1]))))==7:
                        d[6]=parola
                    else:
                        d[0]=parola

            elif len(parola)==5:
                    if len(set(list(d[1])+list(parola)))==len(list(parola)):
                        d[3]=parola
                    elif len(set(list(d[4])+list(parola)))==7:
                        d[2]=parola
                    else:
                        d[5]=parola

        f+=int(output(elem[1],d))

    return gg,f
f=(maddogwayne(l))
print('PT1:',f[0],'\nPT2:',f[1])
