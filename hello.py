# print("hello world")
# #comments in python
# '''
# print(hello) 
# '''
# #variables 
# a = 12
# b = 78
# c = 4
# a  = b
# b = c
# c = a
# print(a)
# print(b)
# print(c)

# name = "abc"
# print(name)
# a = int(input("enter the value"))
# b = float(input("enter the float value"))

# print(b)
# print(type(b))

# is_value = True
# print(type(is_value))

#primitive - number - int ,float, double,str,boolen,

# a = 678689.80980
# print(type(a))
# #non primitive
# name = ("raj","john","ram",78,34) #immtable
# ages = [56,78,23,90]#mutable
# print(type(name))
# print(type(ages))
# print(ages)

# books = {
#     'bookname' :'maxin',
#     'published':'1997'

# }
# print(type(books))

# dep = {"csc","csd","ece"}
# print(type(dep))
# conditional statement
# if statement
# a = int(input(" enter the value "))
# if a>=18:
#     print("you are eligible for the vote")
#even/odd
# a = int(input("enter the value"))
# if a%2 == 0:
#     print("you entered value is even")
# else:
#     print("you entered value is odd")
# b =int(input("enter the value "))

# if b == True:
#     print("hello world")
#python function 
# synax
# def function_name:
#    funtionality

# function_name()
#reusablity,

#step: 1. create the function
#step:2. user will give the input values 
#step:3.which value is bigger among a and b



# def certification():
#     std1 = float(input("Enter the value in %"))
#     std2 = float(input("Enter the value in % "))
#     std3 = float(input("Enter the value in %"))
#     if std1>std2:
#         print("std1 is having higher percentage")
#     else:
#         att2 = float(input("Enter the attd in %"))
#         att3 = float(input("Enter the attd in %"))
#         if att2>att3:
#             print("std2 have higher attendance")
#         else:
#             print("std3 not get certified")
# certification()
# certification()
#user input to take the two values:

#vote :
#1. 3 people are came for to vote 
#2. take the input 3 ages
#3. above 90: eligible for the vote
#4.above and equal 18 : eligible 
#5.Write who are not eligible for the vote

# def user(a,b,c):
#     if a>90:
#         print("eligible for the vote ")
#     elif (b>18 and b>=18):
#         print("eligible for the vote")
#     elif c<18:
#         print("not eligle")
#     else:
#         print("none of the above")
# user(23,67,8)
# user(2,6,18)




# def eligiblity():
#     a = int(input("enter the age"))
#     if a>=18:
#         print("eligible")
#     else:
#         print("not eligible")

# eligiblity()
# eligiblity()
# eligiblity()

# name = [45,78,90,"raj","ram","rahul"]

# for i in name:
#     if i == "rahul":
#         print("yes the name in the list")
#     else:
#         print("Not in the list")

# hello world
# name = input("enter the text ")
# def palindrome():
#     if name == name[::-1]:
#         print("palindrome")
#     else:
#         print("not a palindrome")

# palindrome()



# import math 
# b = math.sqrt(3)
# print(b)
# c = math.pi
# print(c)


# a = ({'c': 5, 'a': 3, 'b': 2})
# student =[('m', 3), ('a', 3), ('x', 3)]
# for i in student:
#     if i[0] =="m":
#         print("m values are ",i[1])
#     print(i[0]) print(b)
# from collections import Counter
# def maxcount():
#     text = input("enter the text")
#     res = Counter(text).most_common()
#     print("the letter is", res[0][0],"repeated",res[0][1])
# maxcount()
# maxcount()

#exceptional handling 

# try:

#     a= int(input("enter value"))
# except ValueError:
#     print("value is not match")
# except  TypeError:
#     print("type is not match")
def add(a,b):
    a = int(input("enter value a"))
    b = int(input("enter value b"))
    print(a+b)
def mul(a,b):
    a = int(input("enter value a"))
    b = int(input("enter value b"))
    print(a*b)

