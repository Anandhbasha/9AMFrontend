# print("Hello")


# a=10
# # print(a/0)

# print(a/"hjhkjh")

# try:
#     a=20
#     b= int(input("Enter thev value"))
#     print(a/b)
# except ZeroDivisionError:
#     print("please enter above zero")
# except TypeError:
#     print("Please enter the postive")
# except ValueError:
#     print("Please enter the number")



class NegativenumError(Exception):
    pass
try:
    age = int(input("Enter Postive Number"))
    if age < 18:
        raise NegativenumError("Not Eligible")
    print("Number Accepted",age)
except NegativenumError as e:
    print("Custom Error",e)