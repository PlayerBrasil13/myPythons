find_char = input("What do you want to find: ")
str_to_find = input("Where do you want to find: ")
# find_char = "needle"
# str_to_find = "There is no needle here, kid"

found = "Yes"
for ch in find_char:
    if ch not in str_to_find:
        found = "No"
        break

print(found)