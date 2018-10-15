from types import MappingProxyType

d = { 1:'A'}
d_proxy = MappingProxyType(d)
print(d_proxy)
print(d_proxy[1])
d_proxy[2] = 'x'

d_proxy
Out[3]: mappingproxy({1: 'A'})
d_proxy[2] = 'x'
# Traceback
#   File "<ipython-input-4-bc17a9a62754>", line 1, in <module>
#     d_proxy[2] = 'x'
# TypeError: 'mappingproxy' object does not support item assignment
d_proxy
Out[5]: mappingproxy({1: 'A'})
d[2] = 'B'
d_proxy
Out[7]: mappingproxy({1: 'A', 2: 'B'})
d_proxy[2]
Out[8]: 'B'