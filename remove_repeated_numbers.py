my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
aux_list = []

for i in range(len(my_list)):
    if my_list[i] in aux_list:
        continue
    aux_list.append(my_list[i])
my_list = aux_list

print("The list with unique elements only:")
print(my_list)
