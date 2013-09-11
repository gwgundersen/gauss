from google.appengine.ext import ndb
from problemModel import ProblemModel


ANCESTOR_KEY = ndb.Key('All', '1')


class Orm:

    def get_problems(self, title=False):

        return ProblemModel.get_sorted_problems(ancestor_key=ANCESTOR_KEY, title=title)


    def flush_datastore(self):

        problems = ProblemModel.get_ndb_problems(ANCESTOR_KEY)
        for p in problems:
            p.key.delete()


    @classmethod
    def rebuild_datastore(cls):

        data = cls.get_canonical_data()
        for p in data:
            problem = ProblemModel(number=p[0], answer=p[1], title=p[2], parent=ANCESTOR_KEY)
            problem.put()


    @classmethod
    def get_canonical_data(cls):

        return [\
            [1, 233168, 'Multiples of 3 and 5'],\
            [2, 4613732, 'Even Fibonacci numbers'],\
            [3, 6857, 'Largest prime factor'],\
            [4, 906609, 'Largest palindrome product'],\
            [5, 232792560, 'Smallest multiple'],\
            [6, 25164150, 'Sum square difference'],\
            [7, 104743, '10001st prime'],\
            [8, 40824, 'Largest product in a series'],\
            [9, 31875000, 'Special Pythagorean triplet'],\
            [10, 142913828922, 'Summation of primes'],\
            [11, 70600674, 'Largest product in a grid'],\
            [12, 76576500, 'Highly divisible triangular number'],\
            [13, 5537376230, 'Large sum'],\
            [14, 837799, 'Longest Collatz sequence'],\
            [15, 137846528820, 'Lattice paths'],\
            [16, 1366, 'Power digit sum'],\
            [17, 21124, 'Number letter counts'],\
            [18, 1074, 'Maximum path sum I'],\
            [19, 171, 'Counting Sundays'],\
            [20, 648, 'Factorial digit sum'],\
            [21, 31626, 'Amicable numbers'],\
            [22, 871198282, 'Names scores'],\
            [23, 4179871, 'Non-abundant sums'],\
            [24, 2783915460, 'Lexicographic permutations'],\
            [25, 4782, '1000-digit Fibonacci number'],\
            [26, 983, 'Reciprocal cycles'],\
            [27, -59231, 'Quadratic primes'],\
            [28, 669171001, 'Number spiral diagonals'],\
            [29, 9183, 'Distinct powers'],\
            [30, 443839, 'Digit fifth powers']
        ]