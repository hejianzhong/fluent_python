class Gizmo():
    def __init__(self):
        print(f"Gizmo id: {id(self)}")

    def __mul__(self, other):
        return [self] * other

    def __repr__(self):
        return str(id(self))

if __name__ == "__main__":
    x = Gizmo()
    print(f"first try to create Gizmo: {x}")
    try:
        y = Gizmo()
        print(f"Second try to create Gizmo: {y * 8}")
    finally:
        print(f" {dir()}")



