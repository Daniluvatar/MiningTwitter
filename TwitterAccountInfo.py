import tweepy


class Profile:

    def __init__(self, api):
        self.api = api

    def following(self):
        following_dic = {}
        for friend in tweepy.Cursor(self.api.friends).items():
            following_dic[friend._json['screen_name']] = friend._json
        return following_dic
