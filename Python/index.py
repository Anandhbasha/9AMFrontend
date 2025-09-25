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
age =20
# if age>=18:
#     print("He is Eligible to Vote")
# else:
#     print("not Eligible")

# elif
# if age>19:
#     print("Adult")
# elif age<13:
#     print("Child")
# else:
#     print("Teenagers")

# nested if

ug=72
hsc=77
sslc=60
if ug>70:
    print("He is Eliglible based on UG Mark")
    if hsc>70:
        print("He is eligible based pn HSC")
        if sslc>=70:
            print("He is elible based on SSLC")
        else:
            print("He is Not elible based on SSLC")
    else:
        print("He is not eligible based pn HSC")
else:
    print("He is not elible")
        
# looping Statements

# while
count = 5
x=0
while count>=x:
    print(x)
    x=x+1


list = [50,88,60,90,44]

# x = 0
# while x<5:
#     print(list[x])
#     x+=1

# for 


for s in list:
    print(s)

for x in range(9):
    print(x)


course = "Python"
rev = ""

for s in course:
    rev = s+rev
print(rev)


# print your name
# input = xyz
# output
# x
# xy
# xyz

# ******
#  *****
#   ****
#    ***
#     **
#      *

# input [50,60,80,90.77]

# Output :[5,6,8,9,14]
# output :41

# array sort

# input :[0,10,0,1,20,8,7]
# Output :[1,7.8,10,20,0,0]

# enter a triple digit number input get a output number in text words