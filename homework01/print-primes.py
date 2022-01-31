# Author: Luke Wilson
# Last Updated: 1/31/2022

import math


for i in range(3,101):
	is_prime = True
	for j in range(2,math.floor(math.sqrt(i))):
		# loop through every number below i to see if its a factor
		if( i % j == 0):
			is_prime = False
			exit		# exits loop when factor is found
	if(is_prime == True):
		print(i)






