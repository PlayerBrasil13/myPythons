birth_date = input("Type your birthday (Format: DDMMYYYY): ")
# print("Type your birthday (Format: DDMMYYYY): 10102010")

def find_digit(birth_date):
    life_digit = int(birth_date)
    birth_list = list(birth_date)
    while life_digit > 9 :
        for digit in range(len(birth_list)):
            birth_list[digit] = int(birth_list[digit])
        life_digit = sum(birth_list)
        birth_list = list(str(life_digit))
    return life_digit

print("Your life digit is: ", find_digit(birth_date))
