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
    #h=[h]
    f=[]
    a=0
    for n in range(1):
        #h.append([])
        f=[]
        print(n)
        for k in range(len(h)):
            #h[-1]=list((h[-1]+r[h[-2][k]]))
            f=f+r[h[k]]
            #print(h[-1])
            #h.remove(h[k])
        print(len(f))
        #h=h[-2:]
        h=f
        del(f)
        a=len(h)
        for n in range(9):
            a+=(len(r[n])-1)*h.count(n)



    return a
#a=[1,2,3]
##b=[4,7,6]
#print(list(a+b))

print(shi(h,128))
'''
a=[2,[3,5,[6,7],[5,3]],[0,43],[5,7]]
from itertools import chain
#print((list(chain.from_iterable(a))))
def iter(subl,l):
    for elem in subl:
        if type(elem)!=list:

            l.append(subl)
        else:
            #for elem in subl:
                l=iter(elem,l)
    return l
def iter2(l):
    

    for elem in l:
        if type(elem)==int:
            h.append(elem)
            l.remove(elem)
            l=(list(chain.from_iterable(a)))
    for elem in h:
        l.append(0)
    return l
'''

