class Average(object):
    def __init__(self):
        self.series = []

    def __call__(self, *args, **kwargs):
        for ele in args:
            self.series.append(ele)

        total = sum(self.series)
        return total / len(self.series)


def make_average():
    series = []

    def average(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)
    return average


if __name__ == "__main__":
    print("calss ========================")
    avg = Average()
    print(f"avg(10): {avg(10)}")
    print(f"avg(11): {avg(11)}")
    print(f"avg(12): {avg(12)}")

    print("method ========================")
    avg = make_average()
    print(f"avg(10): {avg(10)}")
    print(f"avg(11): {avg(11)}")
    print(f"avg(12): {avg(12)}")

    print(avg.__code__.co_names)
    print(avg.__code__.co_freevars)
    print(avg.__code__.co_varnames)
