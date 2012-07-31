'''
Generates a list of prime numbers (Sieve of Eratosthenes) 
'''


def primes(max):
    array=list(range(2,max))
    for num in array:
        notprime=[]
        for y in array[array.index(num):]:
            q=num*y
            #Stop if it becomes bigger than the max number (cant remove a number thats not there)
            if q<=array[-1]:
                notprime.append(q)
            else:
                break
        for z in notprime:
            array.remove(z)
    return array