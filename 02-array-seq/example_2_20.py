from array import array
from random import random

floats1 = array('d', (random() for i in range(10**7)))
print(floats1[-1])

fp = open('floats.bin', 'wb')
floats1.tofile(fp)
fp.close()

fp = open('floats.txt', 'w')
for item in floats1:
    fp.write(str(item) + '\n')
fp.close()

floats2 = array('d')
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10**7)
fp.close()
print(floats2[-1])

print('floats1 == floats2', floats1 == floats2)
