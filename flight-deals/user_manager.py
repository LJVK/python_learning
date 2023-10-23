import requests
from data_manager import DataManager


def check_values(value1, value2):
    if value1 == value2:
        print("You're in the club!")
        return True
    else:
        print("Pls enter your email correctly")
        return False


class UserManager:
    def __int__(self):
        self.sheet_user_post_endpoint = "https://api.sheety.co/08e5b77cd17f84b0925680730e67729d/flightDeals/users"

    data_manager = DataManager()
    print("Welcome to Vijay's Flight Club\nWe find the best flight deals and email you")
    user_first_name = input("What's your first name?:\n")
    user_last_name = input("What's your last name?:\n")
    user_email_1 = input("What's your email?:\n")
    user_email_2 = input("Type your email again:\n")
    if check_values(user_email_1, user_email_2):
        data_manager.post_user_data(user_first_name, user_last_name, user_email_1)
        print("Success! Your Email has been added")
    else:
        user_email_1 = input("What's your email?:\n")
        user_email_2 = input("Type your email again:\n")
        check_values(user_email_1, user_email_2)
