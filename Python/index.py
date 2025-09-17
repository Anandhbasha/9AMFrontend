# print("Welcome to Python" ,end='\t')
# print("this first program of python")

# print('apple',"banana","kiwi",sep='/')

# a=10
# a=20
# print(a)
# b=50
a,b,c=20,50,10

print(a,b,c)

# temp = a
# a=b
# b=c
# c=temp
# print(a,b,c)

b,c,a=a,b,c
print(a,b,c)

# datatypes
    # simple data types
        # int
a=True
print(type(a))
        # float
        # string
        # boolean
    # complex datatypes
        # list
arr = [10,50,77,88,99]
print(arr[0])
print(arr[1])
print(arr[2])
print(arr[3])
        # tuple
data = (45,101,202,808)
print(data)
print(type(data))
        # set
ids = {101,101,102,102,103}
print(ids)
        # dictionary
person = {
    "name":"xyz",
    "age":20,
    "city":"CBE"
}
print(person["name"])


age=18
if age>=18:
    print("He is Eliglible")

def add():
    print("add")
add()
