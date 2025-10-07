from adt import LinkedList

def main():
    # Hardcoded users
    preexisting_users = ["Steven", "Faye", "Rangel", "Gea", "Oxy"]
    title = "Registration System!"
    registered = LinkedList()
    for user in preexisting_users:
        registered.append(user)

    print("=" * len(title))
    print(title)
    print("=" * len(title))
    while True:
        print("Current users registered: ", end ="")
        print(*registered.to_list(), sep=", ")
        action = input("Actions (register/delete/exit): ").strip().lower()
        if action == "register":
            registered_name = input("Enter your name: ").title()
            registered.append(registered_name)
        elif action == "delete":
            deleted_name = input("User to delete: ").strip().title()
            if registered.search(deleted_name) == True:
                registered.delete(deleted_name)
                print("User has been deleted!")
            else:
                print("User does not exist!")
        elif action == "exit":
            break



def get_string(prompt:str) -> str:
    try:
        return input(prompt)
    except ValueError:
        pass
if __name__ == "__main__":
    main()