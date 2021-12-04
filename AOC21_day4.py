f=open('input.txt','r')
r=f.readlines()
input=r[0][:-1].split(',')
r=r[1:]
h=[]
for elem in r:
    if elem=='\n':
        h.append([])
    else:
        if "\n" in elem:
            elem=elem[:-1]
        elem=elem.split()
        h[-1].append(elem)

        
def verify(gruppo):
    for riga in gruppo:
        if ''.join(riga)==len(riga)*'/':
            return True
    ro=[]
    for n in range(len(gruppo)):
        ro.append([])
        for k in range(len(gruppo[n])):
            ro[-1].append(gruppo[k][n])
    for riga in ro:
        if ''.join(riga)==len(riga)*'/':
            return True
    return False

def output(gruppo):
    n=0
    for elem in gruppo:
        for k in elem:
            if k!='/':
                n+=int(k)
    return n

def charm(h,input):
    p=0
    reee = []
    pt1=[]
    for n in range(len(h)):
        reee.append(n)
    for elem in input:
        for gruppo in h:
            for riga in range(len(gruppo)):
                if elem in gruppo[riga]:
                    gruppo[riga][gruppo[riga].index(elem)]='/'


            if verify(gruppo)==True:
                pt1.append(output(gruppo)*int(elem))
                if h.index(gruppo) in reee:
                    reee.remove(h.index(gruppo))
                if len(reee)==0:
                    return pt1[0],output(gruppo)*int(elem)



f=charm(h,input)
print('PT1:',f[0],'\nPT2:',f[1])
