# Python RSS-reader

RSS reader is a command-line utility which receives RSS URL and prints results in human-readable format.

### Requirements
- #### OS
 - Windows
 - Linux
- ### Language
 - Python 3.9

### How to use:

In console input:
 - for Windows: `py rss_reader.py "https://news.yahoo.com/rss/"`
 - for Linux: `python3 rss_reader.py "https://news.yahoo.com/rss/"`


```
usage: rss_reader.py [-h] [--version] [--json] [--verbose] [--limit ] [--date ] [source]

Pure Python command-line RSS reader.

positional arguments:
  source      RSS URL

optional arguments:
  -h, --help  show this help message and exit
  --version   Print version info
  --json      Print result as JSON in stdout
  --verbose   Outputs verbose status messages
  --limit     Limit news topics (should be more or equal to 0) if this parameter provided.
  --date      Specify actual publishing date (should be in format yearmonthday [20211005]) if this parameter provided.
  ```

### Formats of output
#### String format

Array[Feed] \
[Feed]\
|-Title: Блог Onlner\
|-Link: https://blog.onliner.by/ \
|-Date: Thu, 06 May 2021 12:02:26 +0300\
|-Description: Блог Onlner\
|-[IMAGE]\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-Image: https://content.onliner.by/pic/logo.png \
|-[Array[Entries]] \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-[Entry]\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-Title  : МТБанк проводит технические работы с 08.05 по 11.05\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-Link   : https://blog.onliner.by/2021/05/06/mtbank-provodit-texnicheskie-raboty-s-08-05-po-11-05 \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-Date   : Thu, 06 May 2021 12:02:26 +0300 \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-Content: С 8 по 11 мая 2021 (включительно) «МТБанк» проводит

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-[Entry]\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-Title  : МТБанк проводит технические работы с 08.05 по 11.05\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-Link   : https://blog.onliner.by/2021/05/06/mtbank-provodit-texnicheskie-raboty-s-08-05-po-11-05 \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-Date   : Thu, 06 May 2021 12:02:26 +0300 \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-Content: С 8 по 11 мая 2021 (включительно) «МТБанк» проводит

[Feed]\
|-Title: Блог Onlner\
|-Link: https://blog.onliner.by/ \
|-Date: Thu, 06 May 2021 12:02:26 +0300\
|-Description: Блог Onlner\
|-[IMAGE]\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-Image: https://content.onliner.by/pic/logo.png \
|-[Array[Entries]] \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-[Entry]\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-Title  : МТБанк проводит технические работы с 08.05 по 11.05\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-Link   : https://blog.onliner.by/2021/05/06/mtbank-provodit-texnicheskie-raboty-s-08-05-po-11-05 \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-Date   : Thu, 06 May 2021 12:02:26 +0300 \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-Content: С 8 по 11 мая 2021 (включительно) «МТБанк» проводит

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-[Entry]\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-Title  : МТБанк проводит технические работы с 08.05 по 11.05\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-Link   : https://blog.onliner.by/2021/05/06/mtbank-provodit-texnicheskie-raboty-s-08-05-po-11-05 \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-Date   : Thu, 06 May 2021 12:02:26 +0300 \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-Content: С 8 по 11 мая 2021 (включительно) «МТБанк» проводит

#### JSON Schema
```
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "array",
  "items": [
    {
      "type": "object",
      "properties": {
        "id": {
          "type": "string"
        },
        "title": {
          "type": "string"
        },
        "link": {
          "type": "string"
        },
        "image": {
          "type": "object",
          "properties": {
            "title": {
              "type": "string"
            },
            "url": {
              "type": "string"
            },
            "link": {
              "type": "string"
            },
            "width": {
              "type": "string"
            },
            "height": {
              "type": "string"
            },
            "description": {
              "type": "null"
            }
          },
          "required": [
            "title",
            "url",
            "link",
            "width",
            "height",
            "description"
          ]
        },
        "description": {
          "type": "string"
        },
        "published": {
          "type": "string"
        },
        "published_parsed": {
          "type": "array",
          "items": [
            {
              "type": "integer"
            },
            {
              "type": "integer"
            },
            {
              "type": "integer"
            },
            {
              "type": "integer"
            },
            {
              "type": "integer"
            },
            {
              "type": "integer"
            },
            {
              "type": "integer"
            },
            {
              "type": "integer"
            },
            {
              "type": "integer"
            }
          ]
        },
        "entries": {
          "type": "array",
          "items": [
            {
              "type": "object",
              "properties": {
                "id": {
                  "type": "string"
                },
                "title": {
                  "type": "string"
                },
                "link": {
                  "type": "string"
                },
                "description": {
                  "type": "string"
                },
                "description_parsed": {
                  "type": "string"
                },
                "published": {
                  "type": "string"
                },
                "published_parsed": {
                  "type": "array",
                  "items": [
                    {
                      "type": "integer"
                    },
                    {
                      "type": "integer"
                    },
                    {
                      "type": "integer"
                    },
                    {
                      "type": "integer"
                    },
                    {
                      "type": "integer"
                    },
                    {
                      "type": "integer"
                    },
                    {
                      "type": "integer"
                    },
                    {
                      "type": "integer"
                    },
                    {
                      "type": "integer"
                    }
                  ]
                },
                "guid": {
                  "type": "string"
                }
              },
              "required": [
                "id",
                "title",
                "link",
                "description",
                "description_parsed",
                "published",
                "published_parsed",
                "guid"
              ]
            },
            {
              "type": "object",
              "properties": {
                "id": {
                  "type": "string"
                },
                "title": {
                  "type": "string"
                },
                "link": {
                  "type": "string"
                },
                "description": {
                  "type": "string"
                },
                "description_parsed": {
                  "type": "string"
                },
                "published": {
                  "type": "string"
                },
                "published_parsed": {
                  "type": "array",
                  "items": [
                    {
                      "type": "integer"
                    },
                    {
                      "type": "integer"
                    },
                    {
                      "type": "integer"
                    },
                    {
                      "type": "integer"
                    },
                    {
                      "type": "integer"
                    },
                    {
                      "type": "integer"
                    },
                    {
                      "type": "integer"
                    },
                    {
                      "type": "integer"
                    },
                    {
                      "type": "integer"
                    }
                  ]
                },
                "guid": {
                  "type": "string"
                }
              },
              "required": [
                "id",
                "title",
                "link",
                "description",
                "description_parsed",
                "published",
                "published_parsed",
                "guid"
              ]
            }
          ]
        }
      },
      "required": [
        "id",
        "title",
        "link",
        "image",
        "description",
        "published",
        "published_parsed",
        "entries"
      ]
    }
  ]
}
```

### How to install

Download this repo
In root dir run in command line:
`py start.py `