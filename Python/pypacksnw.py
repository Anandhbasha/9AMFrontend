# pip install numpy
import numpy as np

# arr1=np.array([10,20,30])
# print(arr1)

# arr2 = np.array([[20,50,60],[77,88,99]])
# print(arr2)

# arr3 = np.array([[20,50,60],[77,88,99],[558,65645,65454]])
# print(arr3)

# zero = np.zeros([3,4])
# print(zero)

# eyes = np.eye(3)
# print(eyes)

# user_input = input("Enter the value")

# num_list = user_input.split()

# num_list = [int(i) for i in num_list]

# arr = np.array(num_list)
# # print(arr)


# names = "user one"
# newNames = names.split(" ")
# print(newNames)

# onearr = np.ones((2,4))
# print(onearr)

# defRange = np.arange(0,12,2)
# print(defRange)

# equal interval
# equal = np.linspace(0,1,5)
# print(equal)


# 2darray
# # twodarry = np.random.rand(2,2)
# # print(twodarry)

# arr3 = np.array([[20,50,60],[77,88,99],[558,65645,65454]])

# print(arr3[0,1])

# print(arr3[:,1])

# print(arr3[0:3, 1:3])


arr = np.array([10,20,30])
arr1 = np.array([50,60,70])
print(arr[arr>20])
print(arr+arr1)

arr = np.arange(12)
res = arr.reshape(3,4)
print(res)

flat = res.flatten()
print(flat)