import math
f = open('train.txt', 'r')
s = f.read()
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

p = open('3b.in', 'r')
q = p.read()
q=q.replace('\n',' | ')
lines=q.split(' | ')

def shift(letter, number):
	if ord(letter) >= 97 and ord(letter) <= 122:
		new = chr((ord(letter) + number - 97) % 26 + 97)
		return new
	elif ord(letter) >= 65 and ord(letter) <= 90:
		new = chr((ord(letter) + number - 65) % 26 + 65)
		return new
	else: 
		return letter

coeff = [10**(-6), 10**(-5), 10**(-4), 10**(-3), 10**(-2), 10**(-1), 0.888889]
pair = 1
for sen in range(len(lines)):
	if pair == 1:
		size = lines[sen]
		pair = 0
		continue
	else:
		pair = 1
	by = [1] * size
	string = ''
	maxin = 0
	maxsc = -999999
	while True:
		updated = 0
		for i in range(size):
			size[i] += 1
			string = ''
			for letter in range(len(lines[sen])): 
				string += shift(lines[sen][letter], by(letter % size))
			cursc = score(string, coeff)
			if cursc >= maxsc: 
				maxsc = cursc
				maxid = string
				updated = 1
			size[i] -= 1
		if updated == 0:
			break
		sentence = maxid
	
