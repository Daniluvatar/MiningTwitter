"""
Streaming keep the connection to Twitter open, and gather
all the upcoming tweets about a particular event
"""

from tweepy.streaming import StreamListener

# My libraries
from Utilities import Utilities


class MyListener(StreamListener):  # Inherits from StreamListener
    """Custom StreamListener for streaming data."""

    def __init__(self, out_file):
        """
        Class Constructor
        :param out_file:
        """
        super().__init__()
        self.out_file = out_file

    def on_data(self, raw_data):
        """
        This method overrides method in StreamListener
        :param raw_data:
        :return:
        """
        try:
            with open(self.out_file, 'a') as f:
                f.write(raw_data)
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True


    @classmethod
    def fileName(cls, data_path, file_name):
        """
        Factory function to create new MyListener objects
        that generates a formatted json file such as:
        stream_file_name
        :param data_path: Directory path where the json files are going to be stored
        :param file_name:
        :return:
        """
        formatted_name = Utilities.formatFileName(data_path, file_name)
        return cls(formatted_name)

    @classmethod
    def fileNameDate(cls, data_dir, file_name):
        """
        Factory function to create new MyListener objects
        that generates a formatted json file such as:
        stream_file_name_ddmmyyyy
        :param data_dir:
        :param file_name:
        :return:
        """
        formatted_name = Utilities.formatFileName(data_dir, file_name, "date")
        return cls(formatted_name)
