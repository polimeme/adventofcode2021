#Le parti col cancelletto sono utili nel caso la differenza tra le altezze sia solo di 1 e che ogni ogni altezza sfocia in una ed una sola sorgente; questo con la variabile "finito"

f=open('input.txt','r')
r=f.readlines()
for n in range(len(r)):
    r[n]=r[n].replace('\n','')

def clean(l):
    h=[]
    for elem in l:
        if elem not in h:
            h.append(elem)
    return h

def basin(r,n,k,mem):#,finito):
    mem=clean(mem)
    if k < len(r[n]) - 1:
        if  int(r[n][k+1])!=9 and [r[n][k+1],n,k+1] not in mem: #abs(int(r[n][k])-int(r[n][k + 1]))==1 and and [r[n][k+1],n,k+1] not in mem and [r[n][k+1],n,k+1] not in finito:
            mem.append([r[n][k+1],n,k+1])
            a=(basin(r,n,k+1,(mem)))#,finito))
            if type(a) == list:
                mem+=a
    if n < len(r) - 1:
        if int(r[n+1][k])!=9 and [r[n+1][k],n+1,k] not in mem: #abs(int(r[n][k])-int(r[n + 1][k]))==1 and int(r[n+1][k])!=9 and [r[n+1][k],n+1,k] not in mem and [r[n+1][k],n+1,k] not in finito:
            mem.append([r[n+1][k],n+1,k])
            b=(basin(r,n+1,k,mem))#,finito))
            if type(b)==list:
                mem+=clean(b)
    if k > 0:
        if int(r[n][k-1])!=9 and [r[n][k-1],n,k-1] not in mem :#abs(int(r[n][k])-int(r[n][k - 1]))==1 and  int(r[n][k-1])!=9 and [r[n][k-1],n,k-1] not in mem and [r[n][k-1],n,k-1] not in  finito:
            mem.append([r[n][k-1],n,k-1])
            c=(basin(r,n,k-1,mem))#,finito))
            if type(c) == list:
                mem+=clean(c)
    if n > 0:
        if int(r[n-1][k])!=9 and [r[n-1][k],n-1,k] not in mem: #abs(int(r[n][k])-int(r[n - 1][k]))==1 and int(r[n-1][k])!=9 and [r[n-1][k],n-1,k] not in mem and [r[n-1][k],n-1,k] not in finito:
            mem.append([r[n-1][k],n-1,k])
            d=(basin(r,n-1,k,mem))#,finito))
            if type(d)==list:
                mem+=clean(d)

    return clean(mem)


def caleb(r):
        bb=0
        #finito=[]
        mem=[]

        for n in range(len(r)):
            for k in range(len(r[n])):
                mem2=[]
                nano=desu=0
                if k<len(r[n])-1:
                    nano+=1
                    if int(r[n][k])<int(r[n][k+1]):

                        desu += 1
                        mem2.append(int(r[n][k+1]))


                if n<len(r)-1:
                    nano+=1
                    if int(r[n][k])<int(r[n+1][k]):
                        mem2.append(int(r[n+1][k]))
                        desu += 1


                if k>0:
                    nano+=1
                    if int(r[n][k]) < int(r[n][k - 1]):
                        mem2.append(int(r[n][k-1]))
                        desu += 1


                if n>0:
                    nano+=1
                    if int(r[n][k]) < int(r[n-1][k]):
                        mem2.append(int(r[n-1][k]))
                        desu+=1

                if nano==desu:
                    bb+=(int(r[n][k])+1)
                    abbiamo=clean(clean((basin(r,n,k,[[r[n][k],n,k]]))))#,finito))))
                    #finito+=abbiamo
                    mem.append(len(abbiamo))
        gg=1
        for elem in list(reversed(sorted(mem)))[:3]:
            gg*=elem
        return bb,gg

f=caleb(r)
print('PT1:',f[0],'\nPT2:',f[1])



