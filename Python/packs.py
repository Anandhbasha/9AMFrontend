# import math

# print(math.sqrt(25))
# print(math.pow(2,3))
# print(math.pi)

# import random

# print(random.random())
# print(random.randint(1000,9999))
# print(random.choice(["red","blue","white","pink","black"]))

# import datetime

# thisday = datetime.date.today()
# print(thisday)

# timeNow = datetime.datetime.now()
# print(timeNow)

# # os
# import os

# print(os.name)

# print(os.getcwd())

# os.mkdir("application")

# import sys
# print(sys.version)

# # json
# import json
# data = {"name":"xyz","age":20}

# jsonStr = json.dumps(data)

# print(type(jsonStr))

# newValue = json.loads(jsonStr)
# print(type(newValue))


# print(newValue["name"])
# regular expression

import re

# text = "my mobile number 978924571"
# numbers = r'\d{9}'

# match = re.search(numbers,text)
# if match:
#     print("Number Found :",match.group())

# password
# password = "MyPassword1#"
# patt = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[@#$%!_])(?=.*\d).{8,}$'
# if re.match(patt,password):
#     print("Strong Password")

# # # stats
# import statistics
# # val = [10,20,30,40,50]
# # print(statistics.median(val))
# data = [20,40,22,80]
# print(statistics.mean(data))
# print(statistics.median(data))

# collection
# from collections import Counter
# nums = [1,1,1,2,2,3,3,3,3]
# print(Counter(nums))


# # itertolls

import itertools
variable = [1,2,3]
print(list(itertools.permutations(variable,2)))