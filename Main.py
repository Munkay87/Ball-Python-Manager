


import json
from datetime import datetime
snakes = []


def convert_dob(obj):
    if isinstance(obj, datetime):
        return obj.strftime("%d-%m-%Y")


def save_snakes():

    with open("snakes.json", "w") as file:
        json.dump(snakes, file, default=convert_dob)
        print("Snakes saved successfully.")


def load_snakes():
    global snakes
    with open("snakes.json", "r") as file:
        snakes = json.load(file)
        for snake in snakes:
            if snake["dob"] is not None:
                snake["dob"] = datetime.strptime(snake["dob"], "%d-%m-%Y")

snake1 = {
    "id": "BP-0001",
    "name": "Fred",
    "sex": "Male",
    "morphs": "Mojave, Super Special",
    "dob": datetime.strptime("01-07-2026", "%d-%m-%Y"),
    "weight": 109
}
snakes.append(snake1)

snake2 = {
    "id": "BP-0002",
    "name": "Gio",
    "sex": "Male",
    "morphs": "Mojave, GHI",
    "dob": datetime.strptime("26-06-2026", "%d-%m-%Y"),
    "weight": 116
}
snakes.append(snake2)

snake3 = {
    "id": "BP-0003",
    "name": "Finn",
    "sex": "Male",
    "morphs": "Lavender Albino, Axanthic",
    "dob": datetime.strptime("03-07-2026", "%d-%m-%Y"),
    "weight": 107
}
snakes.append(snake3)

load_snakes()

def add_snake():

    snake_number = len(snakes) + 1
    snake_id = f"BP-{snake_number:04}"

    name = input("New snake name (leave blank if unnamed): ").strip()
    if name == "":
        name = "Unnamed"

    while True:
        sex = input("Is the snake M/F: ").lower()
        if sex == "m" or sex == "f":
            break
        else:
            print("Please enter M or F")
    if sex == "m":
        sex = "Male"
    elif sex =="f":
        sex = "Female"

    
    while True:
        dob = input("Date of Birth (DD-MM-YYYY): ").strip()
        if dob == "":
            dob = None
            break
        try:
            dob = datetime.strptime(dob, "%d-%m-%Y")
            break
        except:
            print("Please enter a valid date.")

 
    while True:
        weight = input("Weight in grams (leave blank if unknown): ").strip()
        if weight == "":
            weight = None
            break
        try:
            weight = int(weight)
            if weight > 0:
                break
            else:
                print("Please enter a valid weight.")
        except:
            print("Please enter a valid weight.")          

    new_snake = {
        "id": snake_id,
        "name": name,
        "sex": sex,
        "morphs": input("What morphs does it have: "),
        "dob": dob,
        "weight": weight
    }
    
    snakes.append(new_snake)

def view_snakes():

    for snake in snakes:

        display_snake(snake)

def search_snakes():

    search_term = input("Enter snake ID, morph or name: ")
    found = False

    for snake in snakes:

        if search_term.lower() == snake["id"].lower() or search_term.lower() == snake["name"].lower() or search_term.lower() in snake["morphs"].lower():

            print("=====================")
            print("SNAKE FOUND")
            print("=====================")
            print()
            display_snake(snake)

            found = True

    if not found:

        print("Snake not found.")

def display_snake(snake):

    print("===============================")
    print("SNAKE RECORD")
    print("===============================")
    print()
    print(f"ID: {snake['id']}")
    print(f"Name: {snake['name']}")
    print(f"Sex: {snake['sex']}")
    print(f"Morphs: {snake['morphs']}")
    if snake["dob"] is None:
        print("Date of Birth: Not recorded")
    else:
        print(f"Date of Birth: {snake['dob'].strftime('%d-%m-%Y')}")
    if snake["weight"] is None:
        print("Weight: Not recorded")
    else:
        print(f"Weight: {snake['weight']} grams")
    print()
    print("===============================")



choice = ""

while choice != "4":

    print("===================")
    print("Ball Python Manager")
    print("===================")
    print()
    print("1. Add Snake")
    print("2. View Snakes")
    print("3. Search Snakes")
    print("4. Exit")
    print()
    choice = input("Choose an option: ")

    if choice == "1":

        add_snake()

    elif choice == "2":

        view_snakes()

    elif choice == "3":

        search_snakes()

    elif choice == "4":

        print("Goodbye!")



save_snakes()