'''


A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

'''

def p9(target):
	for i in xrange(1,1000):
		for j in xrange(1,1000):
			if (i**2 + j**2)**0.5 + i +j >target:
				break
			elif (i**2 + j**2)**0.5 + i +j ==target:
				return i*j*((i**2 + j**2)**0.5)

print p9(1000)