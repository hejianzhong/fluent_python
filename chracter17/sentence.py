import re
import reprlib
from collections.abc import Iterator, Iterable

import cachetools

RE_WORD = re.compile(r"\w+")


class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return "Sentence(%s)" % reprlib.repr(self.text)


if __name__ == "__main__":
    s = Sentence('"The time has come," the Walrus said,' )
    print(isinstance(s, Iterable))

    # 循环方式一
    for word in s:
        print(word)

    # 循环方式二
    it = iter(s)
    print(f"isinstance(it, Iterator): {isinstance(it, Iterator)}")
    while True:
        try:
            print(next(it))
        except Exception as e:
            del it
            break


