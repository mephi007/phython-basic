''' transpose a matrix'''
a = [ [4,8],
	  [3,9],	
	  [15,6]]
tr = [ [0,0,0],
      [0,0,0]]

for i in range(len(a)):
	for j in range(len(a[0])):
		tr[j][i]= a[i][j]
for k in tr:
	print k