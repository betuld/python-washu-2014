def greatest_common_divisor (num1, num2):
	remainder=1
	if num1 ==num2:
		return num1
	if num1 > num2:
		dividend=num1
		divisor=num2
	else:
		dividend=num2
		divisor=num1
	while remainder !=0:
		remainder = dividend % divisor	
		dividend = divisor
		divisor = remainder
	return dividend
	
print greatest_common_divisor(1071,462)
print greatest_common_divisor(1071,1071)
print greatest_common_divisor(462,1071)

def prime_numbers(up):
	mainlist = range(2,up+1)
	for i in mainlist:
		multiples=[]
		for j in mainlist:
			if j%i==0 and j/i>1:
				multiples.append(j)
		mainlist = [item for item in mainlist if item not in multiples]
	return mainlist	

print prime_numbers(2)
print prime_numbers(10)
print prime_numbers(121)


# The three discs are on rod n
# The method to move the three discs to rod n+1
# Number 1 goes to rod (n+1)
# Number 2 goes to rod (n+2)
# Number 1 goes to rod (n+2)
# Number 3 goes to rod (n+1)
# Number 1 goes to rod n
# Number 2 goes to rod (n+1)
# Number 1 goes to rod (n+1)

# Let * be the method to remove three discs
# Use * to move the three discs to an open spot
# Move 3+n th disc to the other spot
# Use * to move the three discs to the spot with the disc with smaller number

#Don't initialize arguments to mutable objects





		
		 	