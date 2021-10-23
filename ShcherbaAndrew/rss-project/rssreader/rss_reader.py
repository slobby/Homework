# -*- coding: utf-8 -*-
"""Main module."""
# if __name__ == "__main__" and __package__ is None:
from sys import path
from os.path import dirname as dir

path.append(dir(path[0]))
# __package__ = "rssreader"


def main() -> None:
    """Excecute as main entry point."""
    import sys
    from rssreader.command_line_parser import get_args

    params = get_args()

    from rssreader.app_logger import get_logger
    from rssreader.get_feeds import get_feeds
    from rssreader.utils import print_to_output, html_converter

    logger = get_logger(__name__)

    try:
        feeds = get_feeds(params)
        print_to_output(feeds, params)
        if params.to_html:
            html_converter(feeds, params.to_html)
    except Exception as ex:
        if hasattr(ex, "message"):
            print(ex.message)
        else:
            logger.error("Error. Unrecognized error has occured", exc_info=1)
            print(
                "Error. Unrecognized error has occured. See log or use --verbose mode"
            )
        sys.exit(1)


if __name__ == "__main__":
    main()
