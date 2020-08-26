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
