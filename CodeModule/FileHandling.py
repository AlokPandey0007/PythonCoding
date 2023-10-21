file1=open("CodeModule/myfile.txt",'r') 

#1st param - directory
#2nd param - Mode - r,w,a,r+(read,write)

print(file1.read())

# reads a single line
print(file1.readline()) 

#reads multiple line and store in dataset
print(file1.readlines())

#We need to close the file after opening
file1.close()

#Second way- in this way we do not need to explicitly close the file.
with open("CodeModule/myfile.txt",'r') as file2:
    pass

#We have opened file in write mode. It will remove the existing data and add the new data.
filewrite=open("CodeModule/myfile.txt",'w')

# writing data in file
filewrite.write("I am added from the code")

#closing the file
filewrite.close()

#APPEND
fileappend=open("CodeModule/myfile.txt",'a')

fileappend.write('\nI am added from code in append mode')

fileappend.close()

with open("CodeModule/myfile.txt",'r') as fileread:
    print(fileread.read())





