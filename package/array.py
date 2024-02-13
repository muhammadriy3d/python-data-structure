from array import *


class Array:

    def __init__(self, length) -> None:
        self.array = []
        self.size = 0
        self.length = length
        for _ in range(0, length):
            self.array += [0]

    def insert(self, item) -> None:
        if (self.size >= self.length):
            self.length *= 2
            for _ in range(self.size, self.length):
                self.array += [0]

        if (item != None):
            self.array[self.size] = item
            self.size += 1

    def indexOf(self, item):
        index = 0
        for _ in range(0, self.size):
            if (self.array[_] == item):
                return index
            index += 1
        return f"Error: Out of bound index list range {index}"

    def toArray(self, type: str) -> array:
        arr = array(type, [])
        for _ in range(0, self.size):
            arr.append(_)

        return arr

    def print(self):
        temp = []
        for i in range(self.size):
            print(temp + [self.array[i]])


def main():
    arr = Array(3)

    arr.insert(2)
    arr.insert(3)
    arr.insert(4)
    arr.insert(5)

    arr.print()

    print("Index: ", arr.indexOf(5))

    arrs = arr.toArray("i")
    print(arrs)


if __name__ == "__main__":
    main()
