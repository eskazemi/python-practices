from user import User
from random import choice

FIRST_NAME = ["Ali", "Hasan", "Karim"]
LAST_NAME = ["Hasani", "Kazemi", "Kamali"]
MOBILE = ["09032356897", "0907818262", "09121012525"]

if __name__ == '__main__':
    for mobile in MOBILE:
        User(choice(FIRST_NAME), choice(LAST_NAME), mobile)

    print(len(User.object_list))
    for user in User.object_list:
        print(user.id, user.fullname)
