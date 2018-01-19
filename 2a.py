g=open('output/2a.out','w')

def readPTB(flagPTB):
    global PTBdata
    if flagPTB==1:
        return
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

    
def counter(data, temp):
    count=data.count(temp)
    # count=0
    # for j in range(len(data)):
    #     for k in range(len(temp)):
    #         if data[j+k]!=temp[k] or len(data)-j<len(temp)-k:
    #             break
    #         if k+1==len(temp):
    #             count+=1
    return count
    
PTBdata=''
f = open('input/2a.in', 'r')
s = f.read()
f.close()
flagPTB=0
flag=0
res={}
i=0
data=''
temp=''
while i<len(s):
    c=s[i]
    i+=1
    if c == '|':
        data=temp
        temp=''
        flag=1
        i+=1
    elif c=='\n':
        if data=='PTB':
            readPTB(flagPTB)
            flagPTB=1
            data=PTBdata
        res[temp]=counter(data, temp)
        towrite=str(res[temp])
        g.write(towrite)
        g.write('\n')
        temp=''
        data=''
        flag=0
    elif c=='<' and len(s)-i>=5:
        if s[i:i+5]=='<unk>':
            i+=4
            if len(s)-i>=1 and s[i+1]==' ':
                i+=1
    elif c=='N' and flag==0:
        Nflag=0
        #didn't consider N before punctuations
        if i>0 and len(s)-i>=2:
            if s[i-1:i+2]==' N ':
                i+=1
                Nflag=1
        elif i==0:
            if s[i:i+2]=='N ':
                i+=1
                Nflag=1
        elif len(s)-i<2:
            if s[i-1:i+1]==' N':
                i+=1
                Nflag=1
        if not Nflag:
            temp+=c
    elif ord(c) >= 97 and ord(c) <= 122:
        temp += chr(ord(c) - 32)
    elif (ord(c) >= 65 and ord(c) <= 90):
        temp+=c

if data=='PTB':
    readPTB(flagPTB)
    flagPTB=1
    data=PTBdata
res[temp]=counter(data, temp)
towrite=str(res[temp])
g.write(towrite)
g.write('\n')
g.close()