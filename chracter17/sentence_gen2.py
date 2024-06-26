import re
import reprlib
from collections.abc import Iterator

RE_WORD = re.compile(r"\w+")


"""
    惰性生成器
"""
class Sentence1:
    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return "Sentence(%s)" % reprlib.repr(self.text)

    def __iter__(self):
        for ele in RE_WORD.finditer(self.text):
            yield ele.group()


"""
    惰性生成器表达式
"""
class Sentence2(Sentence1):
    def __init__(self, text):
        super(Sentence2, self).__init__(text)

    def __iter__(self):
        return (word.group() for word in RE_WORD.finditer(self.text))


if __name__ == "__main__":
    s1 = Sentence1('"The time has come," the Walrus said,')
    for word in s1:
        print(word)

    s2 = Sentence2('"The time has come," the Walrus said,')
    for word in s2:
        print(word)

    # it = iter(s)
    # print(f"isinstance(it, Iterator): {isinstance(it, Iterator)}")
    # while True:
    #     try:
    #         print(next(it))
    #     except Exception as e:
    #         del it
    #         break

