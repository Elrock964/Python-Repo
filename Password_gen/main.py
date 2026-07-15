import secrets
import random

upper_chars = "QWERTYUIOPASDFGHJKLZXCVBNM"
lower_chars = "qwertyuiopasdfghjklzxcvbnm"
special_chars = "!@#$%^&*()-+=?/"
numbers = "1234567890"

def Password(pass_Len):
    part1 = round(pass_Len * (30/100))
    part2 = round(pass_Len * (20/100))

    char_list = []
    for i in range(part1):
        char_list.append(secrets.choice(upper_chars))
        char_list.append(secrets.choice(lower_chars))
    for i in range(part2):
        char_list.append(secrets.choice(special_chars))
        char_list.append(secrets.choice(numbers))

    random.shuffle(char_list)

    result = "".join(char_list)
    return result

while True:
    char_len = int(input("How long is your do you want yourt password: "))
    
    result = Password(char_len)
    print(result)
    print()