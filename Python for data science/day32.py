## tuple 
# it is immutable means we can not change the Value 
# tup = (2,1,3,1)
# print(type(tup))
# print(tup[0])
# tup1 = () this is null tuple
# tup2 = (1,) this is single value tuple
# print(tup[1:3]) # this is slicing in tuple 
## indexing 
# print(tup.index(2)) ## here we give me the value and it return us indexvalue
# print(tup.count(1)) ## gere it count how many times 1 is here in this tuple
## praticse question 1 
# movies = []
# movies.append(input("enter the mov"))
# mov1 = input("enter the first moive:")
# mov2 = input("enter the second moive:")
# mov3 = input("enter the third moive:")
# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)
# print(movies)
## question 2
# palindrome
# list1 = [1,2,3]
# list2 = [1,2,1]
# copy_list2 = list2.copy()
# copy_list2.reverse()
# if(copy_list2 == list2):
#     print("palindrome")
# else:
#     print("not palindrome") 
# question 3 
# list = ["c","d","a","a","b","b","a"]
# print(list.count("a")) 
# list.sort()  
# print(list)
## check this is palindrome or not
list = ["c","d","a","a","b","b","a"] 
copy_list = list.copy()
copy_list.reverse()
if(copy_list == list):
    print("it is palindrome")
else:
    print(" it is not palindrome")    


