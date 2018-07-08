#coding:UTF-8
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

def strToInt(strA):
    return reduce(lambda x, y: x*10+y, map(lambda x:LIST_REF[x], strA))

print(strToInt('1234'))

strTest  = "3.1415926"
print(strTest.index('.'))
print('7' not in strTest)

#查找字符在串中最后一次出现的地方
print(strTest.rindex('.'))

#decorator不带参数
def addMoreInfo(func):
    def wrapper(*args):
        print("Before Calling %s"%func.__name__)
        func(*args)
        print("After calling %s"%func.__name__)

    return wrapper

#decorator带参数
def addMoreInfoV2(text):
    def wrapperL1(func):
        def wrapperL2(*args):
            print("V2 Before Calling %s  %s"% (func.__name__, text))
            func(*args)
            print("V2 After Calling %s   %s"% (func.__name__, text))
        return wrapperL2
    return wrapperL1

#@addMoreInfo
@addMoreInfoV2('hello')
def strToFloat(strA):
    if '.' not in strA:
        return strToInt()
    else:
        dotPos = strA.index('.')
        first_part= strA[:dotPos]
        second_part = strA[dotPos+1:]
        print(first_part + " " + second_part)
        print(strToInt(first_part) + float(strToInt(second_part))/10**len(second_part))

strToFloat("100.23")









