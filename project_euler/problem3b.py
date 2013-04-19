#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?


def is_prime(number):
	for i in range(2,int(number/2)+1) :
		if number % i == 0 :
			return False
	return True

def prime_factors(number) :
	start = 2
	mx = 0
	factors = []
	while number > 1:
		while number % start == 0:
			factors.append(start)
			number /= start
		start = start + 1

	factors.reverse()
	for f in factors:
		if is_prime(f):
			return f


print prime_factors(600851475143)