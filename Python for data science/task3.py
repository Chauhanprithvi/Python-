## write to program to check number is even or odd
num = int(input("enter the number"))
if(num%2==0):
    print("number is even")
else:
    print("number is odd")
 ## write a program to check which number is largest
a = int(input("enter the number of a"))
b = int(input("enter the number of b"))
c = int(input("enter the number of c"))
if(a>b):
    print("A is largest",a)
elif(b>c):
    print("B is largest",b)
elif(c>a):
    print(" c is largest",c)   
## write the program and check the number is multiple of 7 or not
num = int(input("enter the number:"))
if(num%7==0):
    print("number is multiple of 7")
else:
    print("number is not multipe of 7")   
 ## write a program and check the number is positive negative and zero
number = int(input("enetr the number:"))
if(number<0):
    print("number is negative")
elif(number>0):
    print("number is positive")
else:
    print("number is zero")
# check wherter a PERSON IS eligible for vote 
age = int(input("enter the age "))
if(age>=18):
    print("can vote")
else:
    print("can not vote")
## check wheter the number is divisible by both 3 and 5
number = int(input("enter the num"))
if(number%3==0 and number%5==0):
    print("number is divisible by both")
else:
    print("number is not divisible by both") 
 ## check the year is leap year or not
year = int(input("enter the year"))
if(year%4==0):
    print("year is leap")
else:
    print("year is not leap")
    