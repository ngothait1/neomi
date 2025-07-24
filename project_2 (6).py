import re

def display_menu():
    print("============ Menu ============")
    print("1. Save a new entry")
    print("2. Search by ID")
    print("3. Print ages average")
    print("4. Print all names")
    print("5. Print all IDs")
    print("6. Print all entries")
    print("7. Print entries by index")
    print("8. Exit")
    print("=============================")
    return input("Please select an option (1-8) or press Enter to refresh: ")

def input_new_entry():
    ID = input("Enter ID: ")
    name = input("Enter name: ")
    age = input("Enter age: ")
    return ID, name, age

def is_valid_ID(ID):
    return ID.isdigit() and len(ID) in (9, 10)

def is_valid_age(age):
    return age.isdigit() and 0 <= int(age) <= 120

def is_valid_name(name):
    return re.match(r'^[\u0590-\u05FFa-zA-Z\s-]+$', name)

def print_error(input_type):
    match input_type:
        case "ID":
            print("ID must be a number with 9 or 10 digits.")
        case "age":
            print("Age must be a number between 0 and 120.")
        case "name":
            print("Name must contain only letters, spaces, or hyphens.")
        case "exists":
            print("ID already exists.")
        case "data":
            print("Error: no data available.")
        case _:
            print("Invalid input.")

def prompt_continue(repeat=False):
    return input("Repeat the action? (y/n) or press Enter to menu: " if repeat 
                 else "Press Enter to menu: ").lower()

def is_new_ID(ID, state):
    return ID not in state["data"]

def save_new_entry(ID, name, age, state):
    if not is_valid_ID(ID):
        print_error("ID")
    elif not is_new_ID(ID, state):
        print_error("exists")
    elif not is_valid_name(name):
        print_error("name")
    elif not is_valid_age(age):
        print_error("age")
    else:
        state["data"][ID] = (name, age)
        state["data_list"].append(ID)
        state["total_age"] += int(age)
        state["entry_count"] += 1
        print("Entry saved successfully.")

def search_ID(ID, state):
    data = state["data"]
    if not data:
        print_error("data")
    elif ID in data:
        name, age = data[ID]
        print(f"ID {ID} exists: ID={ID}, Name={name}, Age={age}")
    else:
        print(f"ID {ID} does not exist.")

def print_ages_average(state):
    if state["entry_count"] == 0:
        print_error("data")
    else:
        print(f"The average is {state['total_age'] / state['entry_count']:.2f}")

def print_names(state):
    data = state["data"]
    if not data:
        print_error("data")
        return
    for ID, (name, _) in data.items():
        print(f"ID={ID}, Name={name}")

def print_IDs(state):
    data = state["data"]
    if not data:
        print_error("data")
        return
    for ID in data:
        print(f"ID={ID}")

def print_all(state):
    data = state["data"]
    if not data:
        print_error("data")
        return
    for ID, (name, age) in data.items():
        print(f"ID={ID}, Name={name}, Age={age}")

def print_by_index(state):
    data_list = state["data_list"]
    data = state["data"]
    if not data_list:
        print("No data.")
        return
    index = input("Enter index: ")
    if not index.isdigit() or not (0 <= int(index) < len(data_list)):
        print("Invalid index.")
        return
    ID = data_list[int(index)]
    name, age = data[ID]
    print(f"ID={ID}, Name={name}, Age={age}")

def main():
    state = {
        "data": {},
        "data_list": [],
        "total_age": 0,
        "entry_count": 0
    }

    while True:
        choice = display_menu()
        if choice == "":
            continue
        if choice not in map(str, range(1, 9)):
            print(f"Invalid choice: {choice}")
            continue
        match choice:
            case "1":
                while True:
                    ID, name, age = input_new_entry()
                    save_new_entry(ID, name, age, state)
                    if prompt_continue(repeat=True) != "y":
                        break
            case "2":
                while True:
                    ID = input("Enter ID to search: ")
                    if not is_valid_ID(ID):
                        print_error("ID")
                        continue
                    search_ID(ID, state)
                    if prompt_continue(repeat=True) != "y":
                        break
            case "3":
                print_ages_average(state)
                prompt_continue()
            case "4":
                print_names(state)
                prompt_continue()
            case "5":
                print_IDs(state)
                prompt_continue()
            case "6":
                print_all(state)
                prompt_continue()
            case "7":
                print_by_index(state)
                prompt_continue(repeat=True)
            case "8":
                if input("Are you sure you want to exit? (y/n): ").lower() == "y":
                    print("Goodbye!")
                    break

if __name__ == "__main__":
    main()

