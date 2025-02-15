# Homework 3.1
hat_list = [1, 2, 3, 4, 5]
print(len(hat_list))

num = int(input("Enter a number: "))
hat_list[2] = num
hat_list.pop()
print(len(hat_list))


# Homework 3.3
# The bubble sort
my_list = []
my_range = int(input("Enter a range: "))

for i in range(my_range):
    add = int(input("Enter a number to add: "))
    my_list.append(add)

print('My list: ', my_list)

swapped = True
while swapped:
    swapped = False
    for i in range(len(my_list)-1):
        if my_list[i] > my_list[i+1]:
            swapped = True
            my_list[i], my_list[i+1] = my_list[i+1], my_list[i]

print('Sorted list: ', my_list)


# Homework 3.5
# split()
my_list = [int(i) for i in input('Enter a list: ').split()]
print('Sum list: ', sum(my_list))
