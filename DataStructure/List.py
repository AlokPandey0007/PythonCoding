#create list. It allow duplicate
mylist = ["apple", "banana", "cherry"]

print(mylist)

#loop list

for i in mylist:
    print(i)

#add item in the list
mylist.append('pineapple')
print(mylist)

#get list item with index
print(mylist[0])

#remove item from the list  
mylist.remove('apple')

mylist.pop()

del mylist[1]

print(mylist)

#sort list
mylist.sort()

#reverse sorting descending
mylist.sort(reverse=True)

#copy list
list2=mylist.copy()

#join list
list3= list2+mylist

