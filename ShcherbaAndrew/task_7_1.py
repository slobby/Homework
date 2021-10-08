#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class FileManager:
    def __init__(self, filename, mode="r", encoding="utf-8"):
        self._filename = filename
        self._mode = mode
        self._encoding = encoding
        self._file = None

    def __enter__(self):
        self._file = open(self._filename, self._mode, encoding=self._encoding)
        return self._file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self._file is not None:
            self._file.close()
        if exc_type:
            print(exc_type, exc_value, exc_traceback)
            return True


if __name__ == "__main__":
    fm = FileManager("test.csv")
    with fm as f:
        print(f.readline())
        f.write("Blabla")

    print("HEY")
