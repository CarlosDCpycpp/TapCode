import Summary
import tap_code_explanation
from encryptor import encrypt
from encryptor import rev_encrypt


def prepare(str_):
    return str_.lower().replace(" ", "")


def print_a():
    print("\nInsert the modifier you would like to apply.\nONE PER INPUT\n"
          "If tou want see the list input: help\n"
          "When you are done input: done\n")


def main():
    print("Tap Code\n\n"
          " For more info in what tap code is input: help\n\n"
          " To encrypt input: encrypt\n"
          " To decrypt input: decrypt\n"  
          " To terminate the program input: exit\n\n")

    while True:

        input_ = prepare(input(" -> "))

        if input_ == "help":
            tap_code_explanation.explain()

        if input_ == "encrypt":
            while True:
                str_ = input("Insert Message: ")
                if str_ != "":
                    break
                else:
                    print("You've inserted an empty string.\nTry again.")
            details = []
            input_a = prepare(input("Would you like to add any modifiers to your message?\nIf so input: Y \n\n ->"))
            if input_a == "y":
                print_a()

                possible_details = ["Reverse", "ReverseWords", "NoSpaces", "Trim", "ChangeCharSep", "ChangeWordSep"]

                while True:
                    input_b = input("Modifier: ")
                    if prepare(input_b) == "help":
                        Summary.summary_dec()
                    elif prepare(input_b) == "done":
                        break
                    elif input_b in possible_details:
                        if input_b == "ChangeCharSep" or input_b == "ChangeWordSep":
                            asd = input("What would you like the new seperator to be?\n -> ")
                            input_b1 = (input_b, asd)
                        else:
                            input_b1 = input_b

                        details.append(input_b1)
                        print(f"{input_b1} added")
                    else:
                        print("That's not a modifier!")

            output = encrypt(str_, *details)
            print(output)

        elif input_ == "decrypt":
            while True:
                str_ = input("Insert Message: ")
                if str_ != "":
                    break
                else:
                    print("You've inserted an empty string.\nTry again.")
            details = []
            input_a = prepare(input("Would you like to add any modifiers to your message?\nIf so input: Y \n\n ->"))
            if input_a == "y":
                print_a()

                possible_details = ["Reverse", "ReverseWords", "NoSpaces", "Trim", "Replace", "ChangeSep",
                                    "Upper1stLetter", "Upper1stLetterEachWord", "UpperAll", "CamelCase", "SnakeCase"]

                while True:
                    input_b = input("Modifier: ")
                    if prepare(input_b) == "help":
                        Summary.summary_rev_dec()
                    elif prepare(input_b) == "done":
                        break
                    elif input_b in possible_details:
                        if input_b == "ChangeCharSep" or input_b == "ChangeWordSep":
                            asd = input("What would you like the new seperator to be?\n -> ")
                            input_b1 = (input_b, asd)
                        else:
                            input_b1 = input_b

                        details.append(input_b1)
                        print(f"{input_b1} added")
                    else:
                        print("That's not a modifier!")

            output = rev_encrypt(str_, *details)
            print(output)

        elif prepare(input_) == "exit":
            break

        else:
            print()


if __name__ == "__main__":
    main()

exit(f"\nProgram Terminated\n\n")
