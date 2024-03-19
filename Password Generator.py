#Program for password generator
import random
import string
print("\t\t\t\t\t\t*PASSWORD GENERATOR*")
print("\t\t\t\t\t\t<------------------>")
while True:
    length_of_password = input("Enter the lenth of password: ")
    if length_of_password.isdigit():
        length_of_password=int(length_of_password)
        print("EASY:      1\nMEDIUM:    2\nHARD:      3\nVery Hard: 4 ")
        complexity = input("Complexity level(1 TO 4): ")
        print()
        if complexity == "1":
            character = string.ascii_lowercase
            print("Generated Password =", end=" ")
            for i in range(length_of_password):
                password = random.choice(character)
                print(password, end="")
            print()
        elif complexity == "2":
            character = string.ascii_letters
            print("Generated Password =", end=" ")
            for i in range(length_of_password):
                password = random.choice(character)
                print(password, end="")
            print()
        elif complexity == "3":
            character = string.ascii_letters + string.digits
            print("Generated Password =", end=" ")
            for i in range(length_of_password):
                password = random.choice(character)
                print(password, end="")
            print()
        elif complexity == "4":
            character = string.ascii_letters + string.digits + string.punctuation
            print("Generated Password =", end=" ")
            for i in range(length_of_password):
                password = random.choice(character)
                print(password, end="")
            print()
        else:
            print()
            print("   --<ERROR>--   \nEnter from 1 to 4 !")
        print()
    else:
        print()
        print("   --<ERROR>--   \nEnter INTEGERS only !")
    print()