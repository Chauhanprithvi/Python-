## List : it is store set of value 
marks = [94.4,87.5,95.2,66.4,45.1]
print(marks)
print(type(marks))
print(marks[0])
print(len(marks))
students = ["prithvi",85,19.5,"ahmedabad"]
print(students[0])
students[0] = "ravi" # change the value
print(students)
print(marks[0:3]) ## here it include 0 and but not include 3
print(marks[0:])  
print(marks[:5])
## negative listing means negative slicing
print(marks[-3:-1]) 
# list method
list = [2,1,3]
list.append(4) ## append use for add the one element in last
print(list)
list.sort()
print(list)
list.sort(reverse=True) ## it give the descending oreder
print(list)
list.reverse()
print(list)
list.insert(1,10)  ## IT change the value given index num
print(list)
list.remove(10)
print(list)
list.pop(3) # it remove the element  from given index number 
print(list)










