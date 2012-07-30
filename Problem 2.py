
def p2(array):
	array.append(array[-1] + array[-2])
	if array[-1]>4000000:
		print sum([i for i in array if i%2 == 0])
		return 0
	p2(array)

p2([1,2])
