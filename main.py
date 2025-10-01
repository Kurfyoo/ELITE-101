import sys
import os
import toolbox as tb

def intro():
    print("""
██████╗ ██████╗ ███████╗ ██████╗     ██╗    ██████╗  █████╗ 
██╔══██╗██╔══██╗██╔════╝██╔════╝    ███║   ██╔═████╗██╔══██╗
██║  ██║██║  ██║█████╗  ██║         ╚██║   ██║██╔██║╚█████╔╝
██║  ██║██║  ██║██╔══╝  ██║          ██║   ████╔╝██║██╔══██╗
██████╔╝██████╔╝███████╗╚██████╗     ██║██╗╚██████╔╝╚█████╔╝
╚═════╝ ╚═════╝ ╚══════╝ ╚═════╝     ╚═╝╚═╝ ╚═════╝  ╚════╝ 
    """)
    print("\tThe Dunking Doughnuts Employment Chatbot")

def get_info():
    name = input("What is your name? ").title()
    tb.wait()
    age = int(input("How old are you? "))
    return name,age

def greet_user(name,age):
    if age < 16:
        print("Welcome, "+name+". You are "+str(16-age)+" year(s) younger than my creator!")
    elif age == 16:
        print("Welcome, "+name+". My creator's the same age!")
    else:
        print("Welcome, "+name+". You are "+str(age-16)+" year(s) older than my creator!")

class MenuHandler:
    def zero():
        pass
    def one():
        pass
    def two():
        pass
    def three():
        pass
    def exit():
        os.system("clear")
        print("Glad if I could help. Goodbye!")
        sys.exit()
actions = [MenuHandler.zero, MenuHandler.one, MenuHandler.two, MenuHandler.three, MenuHandler.exit]

def menu():
    options = ["zero","one","two","three","exit"]
    print("How can I help you?\n")
    for idx, opt, in enumerate(options):
        print(f"{idx}) {opt}")
    choice = int(input("\nEnter a number (0-4): "))
    os.system("clear")
    actions[choice]()
    return choice == 4

def main():
    os.system("clear")
    intro()
    tb.wait()
    name,age = get_info()
    tb.wait()
    greet_user(name,age)
    tb.wait()
    want_exit = False
    while not(want_exit):
        want_exit = menu()
        tb.wait()
if __name__ == "__main__":
    main()
