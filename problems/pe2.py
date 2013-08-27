"""----------------------------------------------------------------------------
Project Euler
Gregory Gundersen
2013-01

Problem:
Each new term in the Fibonacci sequence is generated by adding the previous two
terms. By starting with 1 and 2, the first 10 terms will be:
    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms.

Solution:
Lazy load Fibonacci numbers, testing if each one is divisible by 2.
----------------------------------------------------------------------------"""

import lib.gmath as g


def main():

    result = 0
    gen = g.gen_fibonacci()
    fib = gen.next()
    while fib < 4000000:
        if fib % 2 == 0:
            result += fib
        fib = gen.next()
    return result