# PYTHON PROGRAM TO FIND SMALLEST NUMBER IN A LIST
values = [10, 20, 5, 45, 99]
print("Smallest element is:", min(values))
print()

# PYTHON PROGRAM TO FIND SMALLEST NUMBER IN A LIST
print("Smallest element is:", max(values))
print()

# PYTHON PROGRAM TO FIND SECOND LARGEST NUMBER IN A LIST
values = [10, 20, 70, 45, 99]
values.sort()
print("Second largest element is:", values[-2])
print()

# PYTHON PROGRAM TO PRINT EVEN NUMBERS IN A LIST
list1 = [10, 21, 4, 45, 66, 93, 12, 96, 11]
for num in list1:
   if num % 2 == 0:
       print(num, end=" ")
print()
print()


# PYTHON PROGRAM TO PRINT ODD NUMBERS IN A LIST
for num in list1:
    if num % 2 != 0:
        print(num, end=" ")
print()
print()



#PYTHON PROGRAM TO PRINT ALL ODD NUMBERS IN A RANGE
startValue, endValue = 2, 20
for num in range(startValue, endValue + 1):
    if num % 2 != 0:
        print(num, end=" ")
print()




