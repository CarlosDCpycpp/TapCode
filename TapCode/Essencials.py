import os


def terminate():
    if os.name == 'nt':
        import msvcrt
        print("\n\nPress any key to exit...")
        msvcrt.getch()
    else:
        print("\n\nPress any key to exit...")
        input()
