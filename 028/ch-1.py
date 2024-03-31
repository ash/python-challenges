# Solution of Task 1 of The Weekly Challenge 28
# https://theweeklychallenge.org/blog/perl-weekly-challenge-028

# $ python3 ch-1.py
# 19:03:41

import datetime

now = datetime.datetime.now()
print("%02i:%02i:%02i" % (now.hour, now.minute, now.second))
