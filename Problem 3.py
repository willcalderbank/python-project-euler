'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

from prime import primes

def p3(number):
    for p in reversed(primes(10000)):
        if p*p > number: break
        if number % p == 0:
           return p

print p3(600851475143)