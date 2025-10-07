# bikeName = "pulsar"
# noWheels = 2
# petrolTank = 10
# cc=125

# def brakes():
#     print("Bike stops")
# def acc():
#     print("Bike moves")

# brakes()
# acc()

# class bike:
#     bikeName = "pulsar"
#     noWheels = 2
#     petrolTank = 10
#     cc=125
#     def brakes(self):
#         print(f'{self.cc} Bike Stops')
#     def acc(self):
#         print(f"{self.cc} Bike moves")

# b = bike()
# b.cc=150

# b1 = bike()
# b1.cc=160
# b1.acc()
# b.acc()

# encapsulation

# private variable
# __vari

# class BankAccount:
#     __balance = 500
#     def deposit(self,amount):
#         if amount >0:
#             self.__balance+=amount
#             print(f'{amount} is credited ')
#         else:
#             print("Invalid Amount")
#     def withdraw(self,amount):
#         if 0 <amount <=self.__balance:
#             self.__balance-=amount
#             print(f'{amount} is Debited ')
#         else:
#             print("Insufficient Balance Amount")
#     def showBalance(self):
#         return self.__balance
    

# user1 = BankAccount()
# # user1.deposit(1000)
# # print(user1.showBalance())
# # user1.withdraw(1500)
# # print(user1.showBalance())
# user1.__balance=5000
# print(user1.__balance)
# print(user1.showBalance())

# inheritence
# single inheritence
# class A:    
#     print("Parent Class")
# class B(A):
#     print("Child Class")


class vechicle:
    def brake(self):
        print("Vehicle Stops")
class car(vechicle):
    def acc(self):
        print("Car moves")
    
c = car()
c.brake()
c.acc()