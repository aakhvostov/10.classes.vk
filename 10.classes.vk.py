from urllib.parse import urlencode
import requests


class User:
    def __init__(self, vk_id):
        self.id = vk_id
        self.friend_list = []

    def __and__(self, other_user):
        common_friends = []
        for friend in self.friend_list:
            if friend in other_user.friend_list:
                common_friends.append(User(friend))
        return common_friends

    def __str__(self):
        return 'https://vk.com/id{}'.format(self.id)

    def get_friends(self):
        URL = f"https://api.vk.com/method/friends.get"
        PARAMETERS = {
            "user_id": self.id,
            "order": "name ",
            "access_token": "10b2e6b1a90a01875cfaa0d2dd307b7a73a15ceb1acf0c0f2a9e9c586f3b597815652e5c28ed8a1baf13c",
            "v": 5.122
        }
        url_requests = "?".join((URL, urlencode(PARAMETERS)))
        resp = requests.get(url_requests)
        self.friend_list = resp.json()["response"]["items"]
        return self.friend_list


def user_input():
    ids = input('Введите id пользователей VK через пробел, для которых необходимо найти общих друзей\n').split()
    user_0 = User(ids[0])
    user_1 = User(ids[1])
    user_0.get_friends()
    user_1.get_friends()
    common_friends = user_0 & user_1
    print(common_friends[0])


user_input()
