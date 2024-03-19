my_string = "Hello, Python!"
try:
    my_string[7] = 'W'  # Trying to replace 'P' with 'W'
except TypeError as e:
    print(e)  # Strings are immutable in Python


my_list = [1, 2, 3, 4]
my_list[2] = 30  # Changing the third element from 3 to 30
print(my_list)  # Output: [1, 2, 30, 4]


original_list = [1, 2, 3]
new_list = original_list  # This copies the reference, not the list
new_list[1] = 200  # Modifies the original list as well
print(original_list)  # Output: [1, 200, 3]

independent_copy = original_list[:]
independent_copy[1] = 20
print(original_list)  # Output: [1, 200, 3]
print(independent_copy)  # Output: [1, 20, 3]

a = 10
b = a
b = 5  # 'a' remains unchanged
print(a)  # Output: 10
print(b)  # Output: 5



lst1 = [1, 2, 3]
lst2 = lst1
lst2.append(4)
print(lst1)



