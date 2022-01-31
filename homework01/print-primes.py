import math

for i in range(3,101):
	is_prime = True
	for j in range(2,i):
		if( i % j == 0):
			is_prime = False
			exit
	if(is_prime == True):
		print(i)






