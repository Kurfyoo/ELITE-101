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
    diff = 16 - age
    if diff > 0:
        if diff == 1:
            print("Welcome, "+name+". You are 1 year younger than my creator!")
        print("Welcome, "+name+". You are "+str(diff)+" year(s) younger than my creator!")
    elif diff == 0:
        print("Welcome, "+name+". My creator's the same age!")
    else: # diff < 0
        if diff == -1:
            print("Welcome, "+name+". You are 1 year older than my creator!")
        print("Welcome, "+name+". You are "+str(-diff)+" years older than my creator!")

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
    actions = [zero, one, two, three, exit]

def menu():
    options = ["zero","one","two","three","exit"]
    print("How can I help you?\n")
    for idx, opt, in enumerate(options):
        print(f"{idx}) {opt}")
    choice = int(input("\nEnter a number (0-4): "))
    os.system("clear")
    MenuHandler.actions[choice]()
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