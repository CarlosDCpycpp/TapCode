import Essencials


def explain():
    grid = [
        [" ", "|", " 1 ", "|", " 2 ", "|", " 3 ", "|", " 4 ", "|", " 5"],
        ["-", "-", " - ", "-", " - ", "-", " - ", "-", " - ", "-", " - "],
        ["1", "|", " A ", "|", " B ", "|", "C/K", "|", " D ", "|", " E"],
        ["2", "|", " F ", "|", " G ", "|", " H ", "|", " I ", "|", " J"],
        ["3", "|", " L ", "|", " M ", "|", " N ", "|", " O ", "|", " P"],
        ["4", "|", " Q ", "|", " R ", "|", " S ", "|", " T ", "|", " U"],
        ["5", "|", " V ", "|", " W ", "|", " X ", "|", " Y ", "|", " Z "]
    ]

    print("""
    Tap code is a sound based communicating system
    that uses a 5x5 grid as the encryptor.

    The first number represents the row and the second the column.
    """)
    for row in grid:
        print(*row)


if __name__ == "__main__":
    explain()
    Essencials.terminate()
