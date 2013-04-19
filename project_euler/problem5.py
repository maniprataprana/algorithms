

#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def is_divisible(number): 
	for i in range(1,21):
		if number%i != 0 :
			return False
	return True


def find_number():
	start = 20

	while True :
		if is_divisible(start) :
			return start
		start += 10

print find_number()