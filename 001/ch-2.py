# Solution to the Task 2 of the Weekly Challenge 1
# https://theweeklychallenge.org/blog/perl-weekly-challenge-001/

# Test run:
# $ python3 ch-2.py
# 1
# 2
# fizz
# 4
# buzz
# fizz
# 7
# 8
# fizz
# buzz
# 11
# fizz
# 13
# 14
# fizbuzz
# 16
# 17
# fizz
# 19
# buzz

for n in range(1, 21):
    if n % 15 == 0:
        print('fizbuzz')
    elif n % 3 == 0:
        print('fizz')
    elif n % 5 == 0:
        print('buzz')
    else:
        print(n)
