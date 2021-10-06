#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class HistoryDict(dict):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._history = []

    def add_to_history(self, k, v) -> None:
        if k in self:
            if self[k] == v:
                return None
        self._history = self._history[-9:] + [k]

    def __setitem__(self, k, v) -> None:
        self.add_to_history(k, v)
        return super().__setitem__(k, v)

    def get_history(self):
        return self._history

    def update(self, other):
        for k, v in other.items():
            self.add_to_history(k, v)
        return super().update(other)


if __name__ == "__main__":
    c = HistoryDict({"a": 1, "s": 2, "d": 3, "f": 4})
    print(c)
    c["s"] = 8
    print(c)
    print(c.get_history())
    c.update(
        {"e": 4, "g": 5, "h": 6, "j": 7, "k": 8, "o": 9, "p": 10, "r": 11, "s": 12}
    )
    c["s"] = 8
    c["s"] = 8
    print(c.get_history())
