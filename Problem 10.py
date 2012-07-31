'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

from prime import primes

def p10():
	return sum(primes(200000))
print p10()