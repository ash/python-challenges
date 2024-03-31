# Solution of Task 1 of The Weekly Challenge 21
# https://theweeklychallenge.org/blog/perl-weekly-challenge-02

# Test run:
# $ python3 ch-1.py 20
# 20
# 2.7182818284590455

import sys

max = 100
if (len(sys.argv) > 1):
    max = int(sys.argv[1])

print(max)

e = 1.0
factorial = 1.0
for n in range(1, max):
    factorial = factorial * n
    e = e + 1.0 / factorial

print(e)
