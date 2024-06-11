def make_average():
    total, count = 0, 0

    def average(new_value):
        # 不可变变量如果有赋值操作的话，会导致其不再是自由变量。nonlocal 关键字可以改变这个结果
        nonlocal total, count
        total += new_value
        count += 1
        return total / count
    return average

if __name__ == "__main__":
    avg = make_average()
    print(f"avg(10): {avg(10)}")
    print(f"avg(11): {avg(11)}")
    print(f"avg(12): {avg(12)}")
