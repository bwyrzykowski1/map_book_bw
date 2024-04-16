from models.data_source import users
from utils.crud import read_friends
from utils.crud import add_user
from utils.crud import search_user
from utils.crud import remove_user
if __name__ == '__main__':
    while True:
        print("Welcome to the menu  ")
        print("1. Read a list of friends ")
        print("2. Add new user ")
        print("3. Search user ")
        print("4. Remove a user ")
        print("0. Exit ")
        menu_option = input("Choose an option: ")
        if menu_option == "0":
            break
        if menu_option == "1":
            read_friends(users)
        if menu_option == "2":
            add_user(users)
        if menu_option == "3":
            search_user(users)
        if menu_option == "4":
            remove_user(users)





