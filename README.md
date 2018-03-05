# Mining Twitter
An elegant way to gather tweets from Twitter using the [Tweepy API](http://docs.tweepy.org/en/v3.5.0/index.html)

OOP principles are used to encapsulate the complexity of Tweepy API. In addition, design patterns are taken into action in this prototype to create a robust code which is closed for modification but open for extension. 

A concrete implementation of the Singleton and Decorator patterns in Python 3 is shown.

For running the program you will need to configure Twitter Streaming API. A good example to configure this is in the Step2 of this [tutorial](http://adilmoujahid.com/posts/2014/07/twitter-analytics/). Configure your API key, API secret, Access token and Access token secret in the *config_twitter.py* script.

The main program is *mining_twitter.py*, remeber to change your working directory in the *data_path* variable.

For gathering data from Twitter based on a search word:
```shell
$python config_twitter.py words
```
For gathering data from a Twitter account:
```shell
$python config_twitter.py accounts
```

Since this is a first version, if you want to search for other words or accounts, you will need to change it in the code. I hope to make this part of the code more dynamic in the next version.
