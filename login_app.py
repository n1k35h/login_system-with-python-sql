import login_system

MENU_PROMPT = """\n --- Login App ---

Please choose one of the following options:

1) Login
2) Sign Up
3) Exit

Your Selection: """

def login_menu():
    connection = login_system.connect() # getting the connection from login_system, which is imported at the beginning of the code
    login_system.create_tables(connection) # connection to the SQL table

    while (user_input := input(MENU_PROMPT)) != "3": # this loop continues until the user enter 3, which will exit the loop
        if user_input == "1":
            username = input("Enter the User Name: ")
            password = input("Enter the Password: ")
            print("\n")
            
            users = login_system.get_all_login(connection, username, password)

            if users:
                print(f"User found: {users}")
            else:
                print("User not found")
            
        elif user_input == "2":
            username = input("Enter New User Name: ")
            password = input("Enter New Password: ")
            print("\n")

            login_system.add_login(connection, username, password)

            print(username, "is added")

        else:
            print("\nInvalid input, please enter 1 - Login, 2 - Sign Up or 3 - Exit. ")

login_menu()