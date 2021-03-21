#!/usr/bin/python3

import timeit

code_to_test = """
from decimal import Decimal, getcontext
getcontext().prec=10000000
sum(1/Decimal(16)**k * 
          (Decimal(4)/(8*k+1) - 
           Decimal(2)/(8*k+4) - 
           Decimal(1)/(8*k+5) -
           Decimal(1)/(8*k+6)) for k in range(100))
"""

elapsed_time = timeit.timeit(code_to_test,number=1)
print('Start count 10M in secomds:')
print(elapsed_time)
