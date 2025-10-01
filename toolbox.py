import os

def wait(clr=True):
    print()
    key = input("PRESS ENTER TO CONTINUE: ")
    while key != "":
        print("INVALID KEY")
        key = input("PRESS ENTER TO CONTINUE: ")
    if clr:
        os.system("clear")