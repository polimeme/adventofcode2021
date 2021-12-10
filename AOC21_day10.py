f=open('input.txt','r')
r=f.readlines()
for n in range(len(r)):
    r[n]=r[n].replace('\n','')

def dang(r):
    score = {')': 3, ']': 57, '}': 1197, '>': 25137}
    score2 = {')': 1, ']': 2, '}': 3, '>': 4}
    d = {'(': ')', '[': ']', '{': '}', '<': '>'}
    h = []
    x,y=0,0
    for k in range(len(r)):
        for n in range(10):
            for elem in ['()', '[]', '{}', '<>']:
                while r[k].count(elem) > 0:
                    r[k] = r[k].replace(elem, '')
        for desu in r[k]:
            if desu in [')', ']', '}', '>']:
                r[k] = ''
                x+=score[desu]
                break

    for n in range(len(r)):
        if r[n] != '':
            y = 0
            elem = r[n]
            s = ''
            if elem != '':
                for k in elem:
                    s += d[k]
                r[n] += str((s[::-1]))
            for f in s[::-1]:
                y = (y * 5) + score2[f]
            h.append(y)


    return x,list(sorted(h))[int(len(h)/2)]
f=dang(r)
print('PT1:',f[0],'\nPT2:',f[1])