

symbol_table = []

def user_choice():
    choice_msg = [
        "Enter 1 for Insert",
        "Enter 2 for Set Attribute",
        "Enter 3 for Free",
        "Enter 4 for LookUp",
        "Enter 5 for Display",
        "Enter 6 for Exit",
    ]

    while True:
        for msg in choice_msg:
            print(msg)

        _user_choice = input('\n Enter your choice from the list: ')

        if _user_choice == '1':
            user_data = input('\n Please enter comma separated data you want to add: ')
            print(insert(user_data))

        if len(symbol_table) == 0:
            print("Symbol table is empty. Please insert data first! \n")
            continue

        elif _user_choice == '2':
            show()

        elif _user_choice == '3':
            user_data = input('\n Please enter variable name you want to search: ')
            print(search(var_name=user_data))

        elif _user_choice == '4':
            user_data = input('\n Please enter variable name you want to update: ')
            print(update(var_name=user_data))

        elif _user_choice == '5':
            len(symbol_table)
            user_data = input('\n Please enter variable name you want to delete: ')
            print(delete(var_name=user_data))

        elif _user_choice == '6':
            break
        else:
            print("You entered a wrong choice. Please try again \n")


user_choice()