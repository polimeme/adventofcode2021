f=open('input.txt','r')
r=f.readlines()
f,p=0,0
p2=0
aim=0
for elem in r:
    elem=elem.replace('\n','')
    elem=elem.split()
    if elem[0]=='forward':
        f+=int(elem[1])
        p2+=aim*int(elem[1])
    else:
        if elem[0]=='up':
            p-=int(elem[1])
            aim-=int(elem[1])
        else:
            p+=int(elem[1])
            aim+=int(elem[1])
print("PT1:",f*p,"\nPT2:",f*p2)