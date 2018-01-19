import math
g=open('output/2b.out','w')
f = open('ptb.train.txt', 'r')
s = f.read()
f.close()
s=s.replace(',','')
s=s.replace("'",'')
s=s.replace('.','')
s=s.replace('$','')
s=s.replace('-','')
s=s.replace('\n','')
s=s.replace('<unk>','')
s=s.replace(' N ','')
s=s.replace(' ','')
s=s.upper()
PTBdata=s
def prob(block, key, coeff):
    global PTBdata
    ret = 0	
    for i in range(len(key) - 1):
        if  counter(PTBdata, key[0 : i + 1]) == 0:
            break
        else:
            ret += coeff[i] * counter(PTBdata, key[0 : i + 2]) / counter(PTBdata, key[0 : i + 1])
    return ret

def score(block, coeff):
    ret = 0
    for i in range(len(block) - 7 + 1):
        temp=prob(block, block[i : 7 + i], coeff)
        if temp==0:
            ret=-1000
        else:
            ret += math.log(temp)
    return ret

def counter(data, temp):
    count=data.count(temp)
    return count


coeff = [10**(-6), 10**(-5), 10**(-4), 10**(-3), 10**(-2), 10**(-1), 0.888889]
f = open('input/2b.in', 'r')
s = f.read()
s=s.replace('\n',' | ')
L=s.split(' | ')
i=0
while i<len(L):
    if score(L[i],coeff)<score(L[i+1],coeff):
        g.write(str(2))
        g.write('\n')
    else:
        g.write(str(1))
        g.write('\n')
    i+=2

g.close()
