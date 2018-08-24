from functools import reduce
from itertools import accumulate
import math
import itertools
import functools


# n = int(input())
# a = range(3, int(input()) + 1, 2)
print(2, *filter(lambda x:
                 map(lambda y: x % y, range(3, int(math.sqrt(x)) + 1, 2)) != 0,
                 (filter(lambda x: x % 10 == 1 or x % 10 == 3 or x % 10 == 7 or x % 10 == 9 or
                                   (x < 10 and x % 10 == 5),
                         range(3, 59, 2))
                  )
                 )
      )
itertools.takewhile()