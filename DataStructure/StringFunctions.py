a='krishna'

#Change to first letter capital
print(a.capitalize())

print(a.casefold())

#to change in upper case
print(a.upper())

#change to lower case
print(a.lower())

#find substring in string
a.find('i')

a.index('i')

#check if string is of specific type
print('is numeric ',a.isnumeric())

print(a.join('Hare'))

#replcace string

print(a.replace('a','aa'))

#remove spaces 
b="   Hello   "
print(b.strip())

#split the string

print(b.split('e'))


#join symbol between each char or element in collection
c=','

print(c.join('Alok'))


#string formatting

name='mike'
num=len(name)*3

print('Hello {}, your lucky number is {}'.format(name,num))

#print the float number in formatting

price=100
quant=3
sale=price*quant

print('For your {:.2f} with price {:.2f} having sale {:.2f}'.format(quant,price,sale))