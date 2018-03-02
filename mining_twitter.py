import sys

# My libraries
from Authentication import Authentication
from HarvestingTweets import BasicHarvestTweets
from GatherTweets import GatherTweetsByWords, GatherTweetsByAccounts

if __name__ == "__main__":
    data_path = "/home/user/TwitterData"
    auth = Authentication()

    if sys.argv[1] == "words":
        gtw = GatherTweetsByWords(BasicHarvestTweets(auth.auth, auth.api),
                                  ["startups", "machinelearning"])
        gtw.gatherTweets(data_path, "words")

    elif sys.argv[1] == "accounts":
        gta = GatherTweetsByAccounts(BasicHarvestTweets(auth.auth, auth.api),
                                     ["Forbes", "businessinsider"])
        gta.gatherTweets(data_path, "accounts")

    else:
        print(sys.argv[1] + " not implemented...")
