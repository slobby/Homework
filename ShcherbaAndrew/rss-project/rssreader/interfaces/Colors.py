import os
import sys
from colorama import init, AnsiToWin32, Fore, Back, Style
from rssreader.constants import RSS_COLORIZE


class Colors():
    RED: str = ""
    GREEN: str = ""
    CYAN: str = ""
    BLUE: str = ""
    MAGENTA: str = ""
    RESET: str = ""
    COLOR_STREAM = None

    def __new__(cls):
        if not hasattr(cls, 'inst'):
            cls.inst = super(Colors, cls).__new__(cls)
        return cls.inst

    def __init__(self):
        if os.environ.get(RSS_COLORIZE, "FALSE") == "TRUE":
            self.init_colorama()

    def init_colorama(self):
        init(wrap=False)
        self.COLOR_STREAM = AnsiToWin32(sys.stdout).stream
        self.RED = Fore.RED
        self.GREEN = Fore.GREEN
        self.CYAN = Fore.CYAN
        self.BLUE = Fore.BLUE
        self.MAGENTA = Fore.MAGENTA
        self.RESET = Fore.RESET
