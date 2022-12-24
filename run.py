import os
import colorama
import time
import Windscreen.py

os.system("clear")

def main():
    items=["Do I need to defrost my windscreen?"]
    print("Select an option:\n")
    for i in range(len(items)):
        print("[" + str(i+1) + "]", items[i])

    answer = input("\nYour choice: ")
    if answer == 1:
        os.system("Windscreen.py 1")

main()