"""
Text designing classses.

For more information about textstyle file, check out
https://docs...
"""


class Color:
    """
    All plate needed colors are store in this class.
    """

    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'


class Style:
    """
    All plate styles are stored in this class.
    """

    clear = '\033[0m'
    bold = '\033[1m'
    dim = '\033[2m'
    italic = '\033[3m'
    underline = '\033[4m'
    blinking = '\033[5m'
    reverse = '\033[7m'
    invisible = '\033[8m'


class Alert:
    """
    Alerts expression designs are stored in this class.
    """

    succeed = Color.green + Style.bold
    failed = Color.red + Style.bold


class Failure:

    def __init__(self, title, suggestions='', link=''):
        self.title = title
        self.suggestions = suggestions
        self.link = link

    def text(self):
        context = '%s%s%s' % (Alert.failed, self.title, Style.clear)
        for suggest in self.suggestions:
            context += '\n~> %s' % suggest
        if self.link:
            context += '\n\n%sFor more information about this error, check out..%s\n%s' % (
                Style.bold, Style.clear, self.link)

        return context


class Succeed:

    def __init__(self, title, notes=''):
        self.title = title
        self.notes = notes

    def text(self):
        context = '%s%s%s' % (Alert.succeed, self.title, Style.clear)
        for note in self.notes:
            context += '\n~> %s' % note

        return context
