f=open('input.txt','r')
r=f.readlines()
h=[]
x2=0
h2=[]
for elem in r:
    x2+=1
    elem=elem.replace('\n','')
    h.append(int(elem))
    if len(h)>2:
        h2.append(sum(h[-3:]))
print(h)
def PT1(h):
    n,x=0,0
    a=h[0]
    while n!=len(h)-1:
        n+=1
        b=h[n]
        if b>a:
            x+=1
        a=b
    return x
print((h2))
print("PT1:",PT1(h))
print("\nPT2:",PT1(h2))

