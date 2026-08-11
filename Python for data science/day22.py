## here we pur topic is conditional formatting
# if-elif-else
age = int(input("enter your age"))
if(age>=18):
    print("he can vote")
elif(age<18):
    print("he can not vote")
# ex 2
light = input("enter the traffic colur")
if(light=="green"):
    print("go")
elif(light=="red"):
                    print("stop")   # identitaion                
elif(light=="yellow"):
                   print("wait")                  
                   print("end of code")
else:
        print("our traffic signal is broken")
## example of this 
marks = int(input("enter the marks"))
if(marks>=90):
        print(" our grade  is","A")
elif(marks>=80 and marks<90):
        print("our grade is","B")
elif(marks>=70 and marks<80):
        print("our grade is","C")
else:
        print("our grade is","D")   