#dictionary creation and print
dic= {'a':'apple','b':'bat','c':'cat'}

print(dic)

#update dictionary
dic['a']='Aeroplane'

print(dic)

#delete item from dictionary
del(dic['c'])

print(dic)

#remove the the specific item
dic.pop('b')

#remove last added item in dictionary
dic.popitem()

#it empty the dictionary
dic.clear()

#check if key is present in dictionary
print('b' in dic)
print('z' in dic)

print(dic.get('a'))

dic['d']='dog'
dic['e']='elephant'

#loop dictionary

for x in dic:   # it will print the keys
    print(x)

#print key and values
for x,y in dic.items():
    print(x,y)

#print all values
for x in dic.values():
    print(x)

#prnt all keys
for x in dic.keys():
    print(x)

#copy dictionary
dic2= dic.copy()