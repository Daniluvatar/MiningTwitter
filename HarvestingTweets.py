import abc
from tweepy import Stream

# My libraries
from StreamingTwitter import MyListener


class HarvestTweets(metaclass=abc.ABCMeta):
    """
    Component Interface
    """
    @abc.abstractmethod
    def gatherTweets(self, data_harvested_path, file_name):
        pass


class BasicHarvestTweets(HarvestTweets):
    """
    Concrete Component
    """

    def __init__(self, auth, api):
        self.auth = auth
        self.api = api

    def gatherTweets(self, data_harvested_path, file_name):
        """
        Uses streaming API
        """
        my_listener = MyListener.fileNameDate(data_harvested_path, file_name)
        twitter_stream = Stream(self.auth,
                                MyListener(my_listener.out_file))
        return twitter_stream


class HarvestTweetsDecorator(HarvestTweets):
    """
    Decorator
    """
    def __init__(self, harvest_tweets):
        self.harvest_tweets = harvest_tweets

    def gatherTweets(self, data_harvested_path, file_name):
        return self.harvest_tweets.gatherTweets(data_harvested_path, file_name)
