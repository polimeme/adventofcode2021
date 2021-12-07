from math import sqrt
l=input()
def devstandard(l):
    m=sum(l)/len(l)
    a=0
    for elem in l:
        a+=pow(elem-m,2)
    return sqrt(a/len(l)-1)
def summa(s,n): #TOO MUCH RECURSIVE FOR PY
    if n>0:
        return summa(s+n-1,n-1)
    else:
        return s
def wayne(l):
    r = []
    for c in range(int((sum(l)/len(l))-devstandard(l)),int((sum(l)/len(l))+devstandard(l))):
        a = 0
        for elem in l:
            #a=summa(a,abs(elem-c)+1)
            #print(abs(elem-c),summa(0,abs(elem-c)+2))
            for k in range(1, abs(elem - c) + 1):
                a += k

        r.append(a)
    return min(r)
print(wayne(l))



