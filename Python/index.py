''' print("Hello python",end='\t')
print("This is first Page of Python")

print("xyz","abc","def","wet",sep='_')


a="hello"

b=10
print(a,b,sep="-") '''
# datatypes
    # simple datatypes
    # premitive
# a=20.5
# a=60
# print(a)
# b="Hello"
# tclass = True
# print(type(tclass))

# # swapping
# # a=20
# # b=30
# # c=40

# # temp = a

# # a=b  # a=30

# # b=c # b=40

# # c=temp #c=20

# # a,b,c=20,30,40
# # c,a,b = a,b,c
# # print(a,b,c)


# # complex Datatypes
# # list
# # arr = [50,60,80,66,44] #arr[0] = 50 arr[1] = 60 arr[2] = 80 arr[3] = 66 arr[4] = 44
# # # print(arr)
# # print(arr[0])
# # print(arr[1])

# # tuple
# x=(101,102,103,104,105)
# print(x)

# # set
# newsets = {201,201,203,202,204,202,205}
# print(newsets)

# # dictionary
# person = {
#     "name":"xyz",
#     "age":24,
#     "city":"CBE",
#     "family":{
#         "dad":"hghjjk",
#         "mom":"hghjghj",
#         "siblings":{
#             "brother":"grfcfd",
#             "sister":"puyygbnb"
#         }
#     }
# }
# print(person["family"])

# operators
# arithmetic Opeartors
# +,-,*,/,%
num1=20
num2=10
# print(num1+num2)
# print(num1-num2)
# print(num1*num2)
# print(num1/num2)
# print(num1//num2)
# print(num1%num2)

# # comparison operator
# # >,<,>=,<=,==
# print(num1>num2)
# print(num1<num2)
# print(num1<=20)
# print(num1>=20)
# print(num1==20)

# Logical Opearators
# AND
# OR
# NOT

# print(num1>num2 and num1==20 and num1<num2)
# print(num1>num2 or num1==20 or num1<num2)

# print(not num1==20)

# membership operator
list = ["red","green","Yellow"]

# print("red" in list)
# print("red" not in list)


a=[1,2,3,4]
b=[1,2,3,4]

c=a

print(a is b)
print(a is c)

# condtional Statements
# if
age =12
if age>=18:
    print("He is Eligible to Vote")
else:
    print("not Eligible")