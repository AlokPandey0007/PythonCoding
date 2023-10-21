a = 10
b=0

try:
    print(a/b)
except ZeroDivisionError:
    print("We have got zero division error")
finally:
    print("Program Finished")

