#Set creation. It stores data in unordered list. it sorts the data and does not keep the insertion order.
# we cannot change the item but we can add or remove the item from set
dataS={'a',3,4,5,6}

print(dataS)

#add item

dataS.add('b')

#add other item
dataS.update('c','d')

print(dataS)


dataR={10,20}

data=dataS.union(dataR)

print(data)