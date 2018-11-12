from operator import mul
from functools import  partial

triple = partial(mul, 3)
print(triple(7))