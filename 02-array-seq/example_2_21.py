from array import array

numbers = array('h', [-2, -1, 0, 1, 2])
memv = memoryview(numbers)
print('length of memoryview:', len(memv))
print('the first element:', memv[0])
#转换成单字节，查看numbers
memv_oct = memv.cast('B')
print(memv_oct.tolist())
memv_oct[5] = 4
#占2个字节的整数的高位字节改成了4
print(numbers)

