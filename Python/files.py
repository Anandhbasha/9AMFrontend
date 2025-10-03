# file = open("new.txt",'r')
# print(file.read())
# file.close()

# filewrite = open("new.txt",'w')
# filewrite.write("This new writing about Python")
# print("Added Succesfully")

# # append
# fileappend = open("new.txt",'a')
# fileappend.write("\n Add this line to existing page")
# print("Appended succesfully")

readnewLine = open("new.txt",'r')
# print(readnewLine.readline())

seperrat =readnewLine.readlines() 
for i in seperrat:
    print(i,end="-")
# print(seperrat)