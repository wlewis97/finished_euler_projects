# Euler discovered the remarkable quadratic formula:
#
# n2+n+41
# It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39. However, when n=40,402+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,412+41+41 is clearly divisible by 41.
#
# The incredible formula n2−79n+1601 was discovered, which produces 80 primes for the consecutive values 0≤n≤79. The product of the coefficients, −79 and 1601, is −126479.
#
# Considering quadratics of the form:
#
# n2+an+b, where |a|<1000 and |b|≤1000
#
# where |n| is the modulus/absolute value of n
# e.g. |11|=11 and |−4|=4
# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.
import sympy as sp #modlue that deals with prime numbers
import math
max_n = 0 #initialises the count of high n gets with function providing all prime solutions
for a in range(-1000,1000): #provides range of all possible value of a
    for b in sp.primerange(-1001,1001): #provides range of all possible values of b, as b must be a prime number itself when n is 0
        tot = 7 #initialises the solution to the quadratic to be a prime so that the while statement can begin
        n = -1 # initialises n
        while sp.isprime(int(tot)) is True: #while loop that continues as long as solution to quadratic is a prime
            n += 1 #itterates through n
            tot = (math.pow(n,2)) + (n*a) + b #excecutes the quadratic and assigns solution to tot
        if n-1 > max_n: # using n-1 as n is the first number to NOT provide a prime solution
            max_n = n-1
            max_a = a #saves a and b of quadratic that reaches highest consecutive primes
            max_b = b
print(max_b*max_a) # prints the product of a and b
