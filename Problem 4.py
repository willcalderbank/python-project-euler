'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

def is_palindrome(number):
		str_num = str(number)
		if str_num[:(len(str_num)/2)] == str_num[(len(str_num)/2):][::-1]:
			return True
		return False


def p4():
	correct = []
	start = 100
	for i in xrange(100,999):
		for j in xrange(100,999):
			if is_palindrome(i * j):
				correct.append(i*j)
				continue
	return sorted(correct)[::-1]

		
print p4()