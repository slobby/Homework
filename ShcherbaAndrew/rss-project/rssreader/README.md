# Python RSS-reader

## Iteration 3

RSS reader is a command-line utility which receives RSS URL and:

- parse RSS page and display results as a human style format or as a json
- save and extract recieved feeds in/from file

### Requirements

- #### OS
- Windows
- Linux
- ### Language
- Python 3.9

### How to install:

#### whithout installation

- Clone this repo
- From dir **_rss-project_** install required packages :
  `pip install -r requirements.txt`

#### whith installation

- From dir **_rss-project_** run commands:
- build a wheel file, by running commands:

`pip install wheel` - install a wheel

`py setup.py bdist_wheel` - build a wheel file

`pip install dist/rss_reader-....whl` - install package

### How to use:

Go to dir **_rss-project/rssreader_**
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

Title: RSS БелТА

Link: https://www.belta.by/
Description: Новости в Беларуси

News [1]

Title : ФОТОФАКТ: В Гомеле открыт первый "Магазин 101"

Link : https://www.belta.by/regions/view/fotofakt-v-gomele-otkryt-pervyj-magazin-101-465897-2021/

Date : Fri, 22 Oct 2021 15:09:00 +0300

Content: В целях повышения обеспечения пожарной безопасности, широкомасштабной работы по предупреждению

возникновения пожаров и безопасности жизнедеятельности в Гомеле открыт первый торговый объект "Магазин 101".

#### JSON Schema

```
{
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
        "source": {
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
                "guid"
              ]
            }
          ]
        }
      },
      "required": [
        "id",
        "source",
        "title",
        "link",
        "description",
        "entries"
      ]
    }
  ]
}
```
