import tweepy
from tweepy import OAuthHandler

# My libraries
import config_twitter


class Authentication:
    """
    Singleton
    """
    # Here will be the instance stored.
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if Authentication.__instance is None:
            Authentication()
        return Authentication.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if Authentication.__instance is not None:
            raise Exception("Authentication class is a singleton!")
        else:
            self.auth = OAuthHandler(config_twitter.consumer_key,
                                     config_twitter.consumer_secret)
            self.auth.set_access_token(config_twitter.access_token,
                                       config_twitter.access_secret)
            self.api = tweepy.API(self.auth, wait_on_rate_limit=True)
            Authentication.__instance = self
