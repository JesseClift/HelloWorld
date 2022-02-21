'''
Jesse Clift
Assignment 10.1
02/20/2022
'''
import os

Directory = input("Enter File Destination: ")
if Directory == "":
    Directory = "."
assert os.path.exists(Directory)

Filename = input("Enter Filename: ")
Name = input("Enter Name: ")
Address = input("Enter Address: ")
PH = input("Enter Phone Number: ")

with open("{}/{}.txt".format(Directory, Filename), 'w') as file:
    file.write(",".join([Name, Address, PH]) + "\n")

with open("{}/{}.txt".format(Directory, Filename), 'r') as file:
    print("{}/{}.txt contents".format(Directory, Filename))
    for line in file:
        print(line)