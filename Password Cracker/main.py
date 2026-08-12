import time 
import itertools

possible_Chars = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@_?.")

print("Welcome to password Carcker! A brute force hacker.")

password_to_crack = input("Enter a password to test:\n")

start = time.time()

counter = 1
char_length = 1

for char_length in range(10):
    password = (itertools.product(possible_Chars, repeat = char_length))
    print()
    print()

    print("Currently working on passwords with", char_length, "characters.")
    print("Time Elapsed: ", round(time.time()-start,4))
    print("We have tried ", counter, "possible password. ")

    for i in password:
        counter += 1

        current_guess = ''.join(i)
        if current_guess == password_to_crack:
            end = time.time()
            timetaken = end - start
            print("Found it in ", timetaken, " seconds and", counter, "attempts")

            print("Thant is ", counter / timetaken, " attempts per second!")
            print("Password composed of:", i)
            exit()