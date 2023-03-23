#Dominick Vona
#78932951

def main():
    terminate = False
    while not terminate:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        option = input("\nPlease enter an option: ")

        if option == "1":
            password = input("Please enter your password to encode: ")
            encoded_pass = encode(password)
            print("Your password has been encoded and stored!\n")

        elif option == "2":
            password = decode(encoded_pass)
            print(f"The encoded password is {encoded_pass}, and the original password is {password}.\n")

        elif option == "3":
            terminate = True


def encode(password):
    encoded_pass = ''
    for num in password:
        encoded_pass += str((int(num) + 3) % 10)

    return encoded_pass


if __name__ == "__main__":
    main()