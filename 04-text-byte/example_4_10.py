fp = open('cafe.txt', 'w', encoding='utf-8')
print(fp)
# <_io.TextIOWrapper name='cafe.txt' mode='w' encoding='utf-8'>
# 默认情况下，open函数采用文本模式，返回一个TextIOWrapper对象
print(fp.write('café'))
# 在TextIOWrapper对象上调用write方法返回写入的Unicode字符数：4
fp.close()
import os
print(os.stat('cafe.txt').st_size)
fp2 = open('cafe.txt')
print(fp2)
# 返回一个TextIOWrapper对象，编码是区域设置中的默认值
print(fp2.encoding)
print(fp2.read())
fp.close()
fp3 = open('cafe.txt', encoding='utf-8')
print(fp3)
print(fp3.read())
fp3.close()
fp4 = open('cafe.txt', 'rb')
print(fp4)
# 'rb'标识指明在二进制模式中读取文件
# 返回的是BufferedReader对象，而不是TextIOWrapper对象
print(fp4.read())
fp4.close()
