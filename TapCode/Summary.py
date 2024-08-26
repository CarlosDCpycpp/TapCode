import Essencials


def summary_dec():
    print("""
    - Reverse
    - ReverseWords
    - NoSpaces
    - Trim
    - ChangeCharSep (uses tuple as the arg w/ the name at 0 and the needed var at 1)
    - ChangeWordSep (uses tuple as the arg w/ the name at 0 and the needed var at 1)
    """)


def summary_rev_dec():
    print("""
    - Reverse
    - ReverseWords
    - NoSpaces
    - Trim
    - Replace (uses tuple as the arg w/ the name at 0 and the needed vars at 1 and 2 respectively)
    - ChangeSep (uses tuple as the arg w/ the name at 0 and the needed var at 1)
    - Upper1stLetter
    - Upper1stLetterEachWord
    - UpperAll              
    - CamelCase (the first letter of each word is capitalized except the first one and removes spaces)              
        e.g.: Hello world -> helloWorld              
    - SnakeCase (put all letters in lower case and changes all spaces to underscores)
        e.g.: Hello World -> hello_world
        """)


if __name__ == "__main__":
    summary_dec()
    summary_rev_dec()
    Essencials.terminate()
