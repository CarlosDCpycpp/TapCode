import Essencials


tap_code = {
    "a": "11",
    "b": "12",
    "c": "13",
    "d": "14",
    "e": "15",
    "f": "21",
    "g": "22",
    "h": "23",
    "i": "24",
    "j": "25",
    "k": "13",
    "l": "31",
    "m": "32",
    "n": "33",
    "o": "34",
    "p": "35",
    "q": "41",
    "r": "42",
    "s": "43",
    "t": "44",
    "u": "45",
    "v": "51",
    "w": "52",
    "x": "53",
    "y": "54",
    "z": "55"
}

rev_tap_code = {v: k for k, v in tap_code.items()}

rev_tap_code["13"] = "(c/k)"


def upper_1st_letter(s):
    if not s:
        return s
    return s[0].upper() + s[1:]


def encrypt(str_, *args):
    # these *args have to be applied to the str_ before encryption
    # else it doesn't work
    for arg in args:
        if arg == "ReverseWords":
            str_ = ' '.join(word[::-1] for word in str_.split())
        if arg == "Trim":
            str_ = str_.strip()
        if arg == "NoSpaces":
            str_ = str_.replace(" ", "")

    output = '-'.join(tap_code.get(char, char) for char in str_.lower())

    for arg in args:
        if arg == "Reverse":
            output = '-'.join(output.split('-')[::-1])

    # these *args are based on tuples
    # and the index of each object
    for arg in args:
        # these cannot be used in the same str
        # IF ChangeCharSep change the "-" to " "
        # I may or may not solve this (eventually)
        if isinstance(arg, tuple):
            if arg[0] == "ChangeCharSep":
                output = output.replace("-", arg[1])
            if arg[0] == "ChangeWordSep":
                output = output.replace(" ", arg[1])

    return output


def rev_encrypt(encoded_str, *args):
    codes = encoded_str.split('-')

    output = ''.join(rev_tap_code.get(code, code) for code in codes)

    for arg in args:
        # just use on of these, they are by order of how they affect the str so just use 1
        if arg == "Upper1stLetter":
            output = upper_1st_letter(output)
        if arg == "Upper1stLetterEachWord":
            output = output.title()
        if arg == "UpperAll":
            output = output.upper()

        if arg == "Reverse":
            output = output[::-1]
        if arg == "ReverseWords":
            output = ' '.join(word[::-1] for word in output.split())
        if arg == "NoSpaces":
            output = output.replace(" ", "")
        if arg == "Trim":
            output = output.strip()

        # just use 1 of the following *args in each iteration of the func
        # else it gets confusing and weird
        if arg == "CamelCase":
            words = output.split()
            output = words[0].lower() + ''.join(word.capitalize() for word in words[1:])
        if arg == "SnakeCase":
            output = output.lower().replace(" ", "_")

        # these *args are based on tuples
        # and the index of each object
        if isinstance(arg, tuple):
            if arg[0] == "Replace":
                output = output.replace(arg[1], arg[2])
            if arg[0] == "ChangeSep":
                output = output.replace(" ", arg[1])

    return output


def prepare(str_):
    return str_.lower().replace(" ", "")


if __name__ == "__main__":
    str_a = encrypt("Hello World!")
    str_b = rev_encrypt(str_a, "CamelCase")
    str_c = rev_encrypt(str_a, "SnakeCase")

    str_z = [str_a, str_b, str_c]

    for str__ in str_z:
        print(str__)

    Essencials.terminate()

