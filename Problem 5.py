'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

def p5():
	count = 1
	for number in xrange(2520,1000000000,2520):
		for demonintor in list(xrange(1,20)):
			#print number, demonintor
			if number % demonintor != 0:
				break
			elif demonintor == 19:
				return number, demonintor
			
print p5()