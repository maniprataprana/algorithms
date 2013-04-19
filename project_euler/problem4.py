#A palindromic number reads the same both ways.
#Find the largest palindrome made from the product of two 3-digit numbers


def is_palindrome(number):
	return str(number)==str(number)[::-1]

def largest_palindrome():
	palindrome = 1
	for n1 in range(100,1000):
		for n2 in range(n1,1000):
			p = n1*n2
			if is_palindrome(p) and p > palindrome :
				#print n1,"	",n2
				palindrome = p

	return palindrome
	


#print is_palindrome(9219)
print largest_palindrome()
