my_list = [1, 2, 3, "Python", 3.14]

print(my_list)

for _ in my_list:
    print(_)

print(enumerate(my_list))
type(enumerate(my_list))

for index, item in enumerate(my_list):
    print(index, item)

