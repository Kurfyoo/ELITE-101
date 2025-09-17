import sys
import os
import refunc as rf

def intro():
    print("Hello, I am the Dunking Doughnuts Employment Chatbot, DDEC!")
def get_info():
    name = input("What is your name? ")
    age = int(input("How old are you? "))
    return name,age
def greet_user(name,age):
    if age < 16:
        print("Welcome, "+name+". You are "+str(16-age)+" year(s) younger than my creator!")
    elif age == 16:
        print("Welcome, "+name+". My creator's the same age!")
    else:
        print("Welcome, "+name+". You are "+str(age-16)+" year(s) older than my creator!")
def choice0():
    pass
def choice1():
    pass
def choice2():
    pass
def choice3():
    pass
def exit():
    os.system("clear")
    print("Glad if I could help. Goodbye!")
    sys.exit()
choices = [choice0, choice1, choice2, choice3, exit]
def menu(name,age):
    print("How can I help you?")
    print("0) [placeholder]")
    print("1) [placeholder]")
    print("2) [placeholder]")
    print("3) [placeholder]")
    print("4) exit")
    option = int(input("Enter a number (0-4): "))
    os.system("clear")
    choices[option]()
    return option
def main():
    intro()
    rf.wait()
    name,age = get_info()
    rf.wait()
    greet_user(name,age)
    rf.wait()
    choice = None
    while choice != 4:
        choice = menu(name,age)
        rf.wait()
if __name__ == "__main__":
    main()
