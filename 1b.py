import string 
 
def blockstep(argument):
	argument = argument.split(' | ')
	operator = argument[0]
	key = argument[1].split(' ')
	key = map(int, key)
	phrase = list(argument[2])
	letters = list(string.ascii_uppercase)
	N= len(key)
	count = 0
	if argument[0] == 'ENCRYPT': 
		for i in range(len(phrase)): 
			if phrase[i] in letters: 
				keyToUse = key[count%N]
				count += 1
				index = letters.index(phrase[i])
				if (index+keyToUse > 25):
					phrase[i] = letters[(index + keyToUse - 26)]
				else: 
					phrase[i] = letters[index + keyToUse]
		return "".join(phrase)

	else:
		for i in range(len(phrase)):
			if phrase[i] in letters:
				keyToUse = key[count%N]
				count += 1
				index = letters.index(phrase[i])
				phrase[i] = letters[index - keyToUse]
		return "".join(phrase)
	

f = open('input/1b.in', 'r')
s = f.read()
f.close()
g=open('output/1b.out','w')
L=s.split('\n')
for ele in L:
	if ele!='':
		g.write(blockstep(ele)+'\n')
g.close()

