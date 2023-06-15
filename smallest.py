#print max and min number
"""numbers = [5, 2, 7, 4, 6, 8, 9]

print(min(numbers))
print(max(numbers))"""

#smallest = numbers[0]

"""for num in numbers[1:]:
    if num < smallest:
        smallest = num
print("The smallest number is:", smallest)"""

#even numbers print
"""numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    if num % 2 == 0:  
        print(num, end=" ")"""

#write a python function that accept a string and count the number of upper and lower case letters
#sample "The quick Brown fox" output: upper value =2 , lower value = 9

#def upper_lower_count()

str = input("Enter a string: ")

up_count=0
l_count=0

for i in range (len('')):
    if i.isupper():
        up_count=+1

    elif i.islower():
        l_count=+1

print (up_count)
print (l_count)
    





#problem5

"""def count_upper_lower(string):
    st = input("Enter a string: ")
    upper_count = 0
    lower_count = 0
    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

(incomplete number 5)"""
