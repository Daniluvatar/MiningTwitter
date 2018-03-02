from HarvestingTweets import HarvestTweetsDecorator
from TwitterAccountInfo import Profile


class GatherTweetsByWords(HarvestTweetsDecorator):
    """
    Concrete Decorator
    """

    def __init__(self, harvest_tweets, words):
        super(GatherTweetsByWords, self).__init__(harvest_tweets)
        self.words = words

    def gatherTweets(self, data_harvested_path, file_name):
        parent = super(GatherTweetsByWords, self)
        twitter_stream = parent.gatherTweets(data_harvested_path, file_name)
        twitter_stream.filter(track=self.words)
        return twitter_stream


class GatherTweetsByAccounts(HarvestTweetsDecorator):
    """
    Concrete Decorator
    """
    def __init__(self, harvest_tweets, accounts_names):
        super(GatherTweetsByAccounts, self).__init__(harvest_tweets)
        self.accounts_names = accounts_names

    def gatherTweets(self, data_harvested_path, file_name):
        parent = super(GatherTweetsByAccounts, self)
        twitter_stream = parent.gatherTweets(data_harvested_path, file_name)
        accounts_ids = self.__getAccountsIds()
        twitter_stream.filter(follow=accounts_ids)
        return twitter_stream

    def __getAccountsIds(self):
        profile = Profile(self.harvest_tweets.api)
        following_dict = profile.following()
        accounts_ids = []
        for a in self.accounts_names:
            try:
                account = following_dict[a]
                accounts_ids.append(account["id_str"])
            except KeyError:
                print(f"You are not following {account} account")
        return accounts_ids
