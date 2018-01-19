import string 

def IC_compute(vector) #organized column
	letters = list(string.ascii_uppercase)\
	ICs = [0]*len(vector)
	N = len(vector[0])*len(vector)
 
	for i in range(len(letters)):
		for j in range(len(vector)):
			matrix[i][j] = vector[j].count(letters[i])
	 
	for i in range(25):
		for j in range(25): 
			ICs[i] += matrix[j][i]	
	
	ICs = 26*ICs/float((N*(N-1)))
	avg = sum(ICs)/len(ICs)
	
			
