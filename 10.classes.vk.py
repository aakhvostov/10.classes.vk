from urllib.parse import urlencode
import requests


class User:
    def __init__(self, vk_id):
        self.id = vk_id
        self.friend_list = []

    def get_friends(self):
        URL = f"https://api.vk.com/method/friends.get"
        PARAMETERS = {
            "user_id": self.id,
            "order": "name ",
            "access_token": "10b2e6b1a90a01875cfaa0d2dd307b7a73a15ceb1acf0c0f2a9e9c586f3b597815652e5c28ed8a1baf13c",
            "v": 5.122
        }
        url_requests = "?".join((URL, urlencode(PARAMETERS)))
        # print(url_requests)
        resp = requests.get(url_requests)
        self.friend_list = resp.json()["response"]["items"]
        return self.friend_list

    # def print(self):
    #     return print(f'https://vk.com/id{self.id}')


def get_common_friends(user_name_1, user_name_2):
    common_friends = {}
    for friend in user_name_1.friend_list:
        if friend in user_name_2.friend_list:
            common_friends[f'https://vk.com/id{friend}'] = User(friend)
    print(common_friends)


def user_input():
    users_dict = {}
    ids = input('Введите id пользователей VK через пробел, для которых необходимо найти общих друзей\n').split()
    for number, user_id in enumerate(ids):
        users_dict[f"user_{number}"] = User(user_id)
    # print(users_dict)
    for vk_user in users_dict.values():
        vk_user.get_friends()
        # vk_user.print()
    get_common_friends(*users_dict.values())


user_input()
