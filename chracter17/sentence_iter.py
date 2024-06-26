"""
    可迭代对象：仅实现__iter__（返回一个迭代器）
    迭代器： 实现了__next__和__iter__（一般返回自身）
"""

import re
import reprlib
from collections.abc import Iterator

WORD_RE = re.compile(r"\w+")


class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = re.findall(WORD_RE, text)

    def __repr__(self):
        return "Sentence(%s)" % reprlib.repr(self.text)

    def __iter__(self):
        return SentenceIterator(self.words)


class SentenceIterator:
    def __init__(self, words):
        self.words = words
        self.index = 0

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return word

    def __iter__(self):
        return self


if __name__ == "__main__":
    s = Sentence('"The time has come," the Walrus said,' )

    it = iter(s)
    print(f"isinstance(it, Iterator): {isinstance(it, Iterator)}")
    while True:
        try:
            print(next(it))
        except Exception as e:
            del it
            break
