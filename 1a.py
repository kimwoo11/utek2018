import string

def simplestep(argument):
	argument = argument.split(' | ')
	operator = argument[0]
	key = int(argument[1])
	phrase = argument[2]
	s = list(phrase) 
	letters = list(string.ascii_uppercase) 

	if (operator == 'ENCRYPT'):
		for i in range(len(s)):
			if s[i] in letters: 
				index = letters.index(s[i])
				if (index+key>25):
					s[i] = letters[index+key-26]
				else: 
					s[i] = letters[index+key]
		return "".join(s)
	else: 
		for i in range(len(s)):
			if s[i] in letters:
				index = letters.index(s[i]) 
				s[i] = letters[index-key]
		return "".join(s)

f = open('input/1a.in', 'r')
s = f.read()
f.close()
g=open('output/1a.out','w')
L=s.split('\n')
for ele in L:
	if ele!='':
		g.write(simplestep(ele)+'\n')
g.close()

