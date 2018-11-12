metro_data = [
    ('Tokyo', 'JP', 36.933, (35.6897222, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.1333333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]
from operator import itemgetter
for city in sorted(metro_data, key=itemgetter(1)):
    print(city)

'''
Output:
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833))
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889))
    ('Tokyo', 'JP', 36.933, (35.6897222, 139.691667))
    ('Mexico City', 'MX', 20.142, (19.433333, -99.1333333))
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386))

'''

cc_name = itemgetter(1, 0)
for city in metro_data:
    print(cc_name(city))

'''
Output:
('JP', 'Tokyo')
('IN', 'Delhi NCR')
('MX', 'Mexico City')
('US', 'New York-Newark')
('BR', 'Sao Paulo')

'''
list_people = [
     {'name': 'Mike', 'age': 22, 'score': 90},
     {'name': 'Alice', 'age': 22, 'score': 90},
     {'name': 'Lee', 'age': 26, 'score': 92},
     {'name': 'Ben', 'age': 26, 'score': 85},
     {'name': 'Tom', 'age': 33, 'score': 90},
     {'name': 'Jill', 'age': 41, 'score': 72}
]

for person in sorted(list_people, key = itemgetter('age', 'name')):
    print(person)

'''
Output:
{'name': 'Alice', 'score': 90, 'age': 22}
{'name': 'Mike', 'score': 90, 'age': 22}
{'name': 'Ben', 'score': 85, 'age': 26}
{'name': 'Lee', 'score': 92, 'age': 26}
{'name': 'Tom', 'score': 90, 'age': 33}
{'name': 'Jill', 'score': 72, 'age': 41}
'''