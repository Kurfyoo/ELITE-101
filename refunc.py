import os

def wait(clr=True):
    print()
    key = input("PRESS ENTER TO CONTINUE: ")
    while key != "":
        print("invalid key")
        key = input("PRESS ENTER TO CONTINUE: ")
    if clr:
        os.system("clear")