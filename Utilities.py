import string
import datetime


class Utilities:

    @staticmethod
    def formatFileName(data_path, file_name, format_type="normal"):  # public method

        if format_type == "date":
            formatted_name = Utilities.__formatFileNameDate(file_name)
        else:
            formatted_name = Utilities.__formatJustFileName(file_name)

        formatted_name = "%s/stream_%s.json" % (data_path, formatted_name)

        return formatted_name

    @staticmethod
    def __formatJustFileName(file_name):  # private method (__nameMethod)
        """Convert file name into a safe string.
        Arguments:
            fname -- the file name to convert
        Return:
            String -- converted file name
        """
        formatted_name = ''.join(Utilities.__convertValid(one_char) for one_char in file_name)
        return formatted_name

    @staticmethod
    def __formatFileNameDate(file_name):
        """Convert file name into a safe string including the current date.
        Arguments:
            fname -- the file name to convert
        Return:
            String -- converted file name
        """
        today = datetime.datetime.now()
        today_format = "%s%s%s" % (today.day, today.month, today.year)
        formatted_name = ''.join(Utilities.__convertValid(one_char) for one_char in file_name)
        formatted_name = formatted_name + "_" + today_format
        return formatted_name

    @staticmethod
    def __convertValid(one_char):
        """Convert a character into '_' if invalid.
        Arguments:
            one_char -- the char to convert
        Return:
            Character -- converted char
        """
        valid_chars = "-_.%s%s" % (string.ascii_letters, string.digits)
        if one_char in valid_chars:
            return one_char
        else:
            return '_'
