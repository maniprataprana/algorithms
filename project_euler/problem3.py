#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?


def is_prime(number):
	for i in range(2,int(number/2)+1) :
		if number % i == 0 :
			return False
	return True

def prime_factors(number) :
	start = 3
	mx = 3

	while start <= int(number/2) :
		if start != 3 or start != 5 or start != 7 :
			if  start % 3 == 0 or start % 5 == 0 or start % 7 == 0 :
				start += 2
				continue 
		elif is_prime(start)  :
			if number % start == 0:
				number = number / start
				mx = start
		start += 2
	return mx


print prime_factors(600851475143)