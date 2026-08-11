## string
#  there are many types we represent string in Python
# 1.'',"","""" str""""
str1 = "Hello,my name is chauhan prithvi.my age is 19"
print(str1)
## use escape funcation
str2 = "Hello,my name is chauhan prithvi.\nmy age is 19"
print(str2) 
# basic operation 
name = "prithvi"
surname = "chauhan"
Full_name = name+" "+surname # here we use concet(+) funcation
print(Full_name)
len1= len(Full_name)
print(len1) # here we use the len funcation
## indexing: it is start with 0 
str = "chauhan_prithvi"
print(str[0]) # here [0] is index value 
print(str[1])
print(str[2])
print(str[3])
print(str[4])
print(str[5])
# ex2
name= "prithvi"
print(name[3])
# slicing: whenever we want to specifica part of string we use it
# formula = nameofstring[staring_index_number:end_index_number]
name = "prithvi"
print(name[1:4]) 
print(name[:len(str)]) ## here we start with 0 and take the last staring
print(name[1:]) ## here it start with 1 and take a full length
print(name[:7]) ## here it start with 0 and go the 7
# negative slicing
## here counting start in backside
fruit = "apple"
print(fruit[-3:-1])
## here we known basic funcation of python
name = "my name is chauhan prithvi"
print(name.endswith("thvi"))
print(name.endswith("th"))
print(name)
print(name.capitalize())
print(name.replace("prithvi","Ravi"))
print(name.find("n")) ## it is give the index_number
print(name.count("i")) ## It is count how many times this word take in sentence
