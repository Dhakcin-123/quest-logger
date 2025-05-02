import random
from datetime import datetime

print("Welcome to the Adventure Quest Logger")
print("The commands are: '/create', '/quit', '/view', '/filter'")
while True:
    command = input("Enter command: ").lower().strip()
    if command == "/quit":
        print("See you later")
        break
    elif command == "/create":
        hero = input("Enetr hero's name: ").strip()
        goal = input("Enter quest goal e.g.(Find treasure): ").lower().strip()
        settings = ["Forest","Castle","Mountains"]
        outcomes = ["Succeded","Struggled","Discovered secrets"]
        quest = f"{hero} set out to {goal} in a {random.choice(settings)} and {random.choice(outcomes)}"
        print("Quest log")
        print(quest)
        with open("quest.txt","a") as f:
            f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {quest}\n")
        print("Quest saved")
    elif command == "/view":
        try:
            with open("quest.txt","r") as f:
                quests = f.read()
            if quests:
                print("\n Past quest")
                print(quests)
            else:
                print("No quests yet")
        except FileNotFoundError:
            print("No quest file created yet")
    elif command.startswith("/filter"):
        keyword = command[8:].strip()
        if not keyword:
            print("Please provide a heroes name: ")
        else:
            try:
                with open("quest.txt","r") as f:
                    lines = f.readlines()
                print("\n Matching quests: ")
                found = False
                for line in lines:
                    if keyword.lower() in line.lower():
                        print(line.strip())
                        found = True
                if not found:
                    print("No stories match that keyword")
            except FileNotFoundError:
                print("No quest file yet")
    else:
        print("Invalid command") 