list_1 = [1]
list_2 = list_1
list_1[0] = 2
print(list_2)

list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)

my_list = [10,8,6,4,2]
new_list = my_list[1:3]
print(new_list)

new_list = my_list[1:-1]
print(new_list)
new_list = my_list[1:-3]
print(new_list)

new_list = my_list
del new_list[0:2]
print(new_list)

del new_list[:]
print(new_list)

new_list = ["A","B",1,2]

print("A" in new_list)
print("B" not in new_list)

