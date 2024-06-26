"""
    生成器版本的Sentence类
    yield
"""

import re
import reprlib
from collections.abc import Iterator

WORD_RE = re.compile(r"\w+")

class Sentence_gen:
    def __init__(self, text):
        self.text = text
        self.words = re.findall(WORD_RE, text)

    def __repr__(self):
        return "Sentence(%s)" % reprlib.repr(self.text)

    def __iter__(self):
        for word in self.words:
            yield word

if __name__ == "__main__":
    s = Sentence_gen('"The time has come," the Walrus said,' )

    it = iter(s)
    print(f"isinstance(it, Iterator): {isinstance(it, Iterator)}")
    while True:
        try:
            print(next(it))
        except Exception as e:
            del it
            break

    def gen_ABC():
        print("start")
        yield "A"
        print("continue")
        yield "B"
        print("end.")
        yield "C"

    for ele in gen_ABC():
        print(f"--> {ele}")