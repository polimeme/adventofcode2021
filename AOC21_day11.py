f=open('input.txt','r')
r=f.read().replace('\n',' ').split()
for n in range((len(r))):
        r[n]=list(r[n])

def lee(r):
    gx=0
    for volte in range(1000):
        x=0
        mem=[]
        for n in range(len(r)):
            for k in range(len(r[n])):
                r[n][k]=str(int(r[n][k])+1)
        y=100
        while y>1:
            y-=1
            for n in range(len(r)):
                for k in range(len(r[n])):
                    if int(r[n][k])>=10:
                        r[n][k]="0"
                        mem.append([n,k])
                        x+=1
                        if volte<100:
                            gx+=1
                        for n1 in [-1,0,1]:
                            for k1 in [-1,0,1]:
                                try:
                                    if [n+n1,k+k1] not in mem and n+n1>=0 and k+k1>=0:
                                        r[n+n1][k+k1]=str(int(r[n+n1][k+k1])+1)
                                except IndexError:
                                    pass

        if volte >= 100 and x==100:
            return gx,volte+1

f=lee(r)
print('PT1:',f[0],'\nPT2:',f[1])

