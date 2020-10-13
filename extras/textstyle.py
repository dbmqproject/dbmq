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

    def __init__(self, title, suggestions=[], link='', prefix=''):
        self.title = title
        self.suggestions = suggestions
        self.link = link
        self.prefix = prefix

    def text(self):
        context = '%s%s%s' % (Alert.failed, self.title, Style.clear)
        for suggest in self.suggestions:
            context += '\n%s%s%s%s' % (self.prefix,
                                       Style.bold, suggest, Style.clear)
        if self.link:
            context += '\n%sFor more information about this error, check out..%s\n%s' % (
                Style.bold, Style.clear, self.link)

        return context

    def title(self):
        return self.title


class Succeed:

    def __init__(self, title, notes=[], prefix=''):
        self.title = title
        self.notes = notes
        self.prefix = prefix

    def text(self):
        context = '%s%s%s' % (
            Alert.succeed, self.title, Style.clear)
        for note in self.notes:
            context += '\n%s%s%s%s' % (self.prefix,
                                       Style.bold, note, Style.clear)

        return context

    def title(self):
        return self.title


class Notification:

    def __init__(self, title):
        self.title = title

    def text(self):
        return '%s%s%s' % (Style.bold, self.title, Style.clear)
