import json
from functools import reduce

print("hello world")

students = {"zhuliang":15, "liangzhu":18}
for name, age in students.items():
    print('name = {0}, age = {1}'.format(name, age))

for name in sorted(students.keys()):
    print('name = {0}'.format(name))

numbers = [1, 2, 3, 4, 5]
with open('json.txt', 'w') as file_obj:
    json.dump(numbers, file_obj)

with open('json.txt') as file_obj:
    data = json.load(file_obj)
    data.append(100)


print("data is")
print(data)

#message  = input("Tell me Siri")

def funcA(x):
    return x*x

listA = list(map(funcA, [1, 2, 3, 4, 5]))

listB = list(map(str, [1, 2 ,3, 4, 5]))

print(listA)
print(listB)

print(list(filter(lambda x: x%2==0, [1, 2, 3, 4, 5])))

LIST_REF = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}

def trans(strA):
    return reduce(lambda x, y: x*10+y, map(lambda x:LIST_REF[x], strA))

print(trans('1234'))


