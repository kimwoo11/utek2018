import string

def permutation(argument):
	argument = argument.split(' | ')
	operator = argument[0]
	key = list(argument[1])
	message = list(argument[2])
	letters = list(string.ascii_uppercase)	

	if(operator == 'ENCRYPT'):
		for i in range(len(message)):
			if message[i] in letters: 
				index = letters.index(message[i])
				message[i] = key[index]
		return "".join(message)
	
	else:
		for i in range(len(message)): 
			if message[i] in key:
				index = key.index(message[i])
				message[i] = letters[index]
		return "".join(message)




f = open('input/1c.in', 'r')
s = f.read()
f.close()
g=open('output/1c.out','w')
L=s.split('\n')
for ele in L:
	if ele!='':
		g.write(permutation(ele)+'\n')
g.close()
