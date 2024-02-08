import time

class LinkedList:
    class Node:
        def __init__(self, value=0):
            self.value = value
            self.next = None

        def set_next(self, node):
            self.next = node

    def __init__(self):
        self.first = None
        self.last = None

    def isEmpty(self):
        return self.first == None

    def dropList(self):
        self.first = self.last = None

    def appendNode(self, node):
        self.first = self.last = node

    def appendNodeFirstBefore(self, node, before):
        node.set_next(before)
        before = node
        return before

    def appendNodeLastBetweenAfter(self, node, after):
        after.next = node
        return after.next

    def insertFirst(self, item):
        node = self.Node(value=item)
        if self.isEmpty():
            self.appendNode(node=node)
        else:
            self.first = self.appendNodeFirstBefore(node, self.first)

    def insertAtIndex(self, index, item):
        node = self.Node(item)
        length = self.size()

        if (index > length or index < 0):
            return f"Error: Out of bound index list size: {length}"

        if (self.isEmpty()):
            self.appendNode(node)
        else:
            i = 0
            currentNode = self.first
            while currentNode != None or (index and i) == length:
                if (index == i):
                    prev = self.getPreviousNode(currentNode)
                    if (currentNode == self.first):
                        self.first = self.appendNodeFirstBefore(
                            node, currentNode)
                    elif (prev == self.last and (index and i) == length):
                        self.last = self.appendNodeLastBetweenAfter(
                            node, self.last)
                    else:
                        shiftedNode = prev.next
                        prev.next = self.appendNodeFirstBefore(
                            node, shiftedNode)

                if (currentNode != None):
                    currentNode = currentNode.next
                i += 1

    def insertLast(self, item):
        node = self.Node(value=item)

        if self.isEmpty():
            self.appendNode(node=node)
        else:
            self.last = self.appendNodeLastBetweenAfter(node, self.last)

    def indexOf(self, item):
        index = 0
        currentNode = self.first
        while (currentNode != None):
            if (item == currentNode.value):
                return index
            currentNode = currentNode.next
            index += 1
        return -1

    def contains(self, item):
        return self.indexOf(item) != -1

    def size(self):
        count = 0
        currentNode = self.first
        while (currentNode != None):
            currentNode = currentNode.next
            count += 1
        return count

    def removeFirst(self):
        if (not (self.isEmpty())):
            if (self.first == self.last):
                self.dropList()
                return

            second = self.first.next
            self.first = None
            self.first = second

    def removeLast(self):
        if (not (self.isEmpty())):
            if (self.first == self.last):
                self.dropList()
                return

            prev = self.getPreviousNode(self.last)
            self.last = prev
            self.last.next = None

    def removeAt(self, index):
        if (not (self.isEmpty()) and not (index < 0) and not (index > self.size())):
            i = 0
            currentNode = self.first
            while (currentNode != None):
                if (index == i):
                    prev = self.getPreviousNode(currentNode)
                    second = currentNode.next
                    prev.next = None
                    prev.next = second
                currentNode = currentNode.next
                i += 1

    def getPreviousNode(self, node):
        currentNode = self.first
        while (currentNode != None):
            if (currentNode.next == node):
                return currentNode

            currentNode = currentNode.next

    def print(self):
        currentNode = self.first
        while (currentNode != None):
            print(currentNode.value)
            currentNode = currentNode.next

    def toArray(self):
        if (self.isEmpty()):
            return []

        list = []
        currentNode = self.first
        while (currentNode != None):
            list.append(currentNode.value)
            currentNode = currentNode.next

        return list


def main():
    linked_list = LinkedList()
    linked_list.insertFirst(20)
    linked_list.insertLast(30)
    linked_list.insertFirst(10)
    linked_list.insertLast(40)
    linked_list.insertFirst(0)

    print(f"""
        LinkedList to array test: 
        {linked_list.toArray()}
    """)

    for arr in linked_list.toArray():
        if (arr == 20):
            continue
        else:
            print(arr)

    print()
    print("list item list size test: ")
    print(f'This list has a size of {linked_list.size()}')

    print()
    print("list item index search test: ")
    print(f"Index of -1 is -1 mean not found:  {linked_list.indexOf(-1)}")
    print(f"Index of 0  is -1 mean not found:  {linked_list.indexOf( 0)}")
    print(f"Index of 10 is -1 mean not found:  {linked_list.indexOf(10)}")
    print(f"Index of 20 is -1 mean not found:  {linked_list.indexOf(20)}")
    print(f"Index of 30 is -1 mean not found:  {linked_list.indexOf(30)}")
    print(f"Index of 40 is -1 mean not found:  {linked_list.indexOf(40)}")
    print(f"Index of 50 is -1 mean not found:  {linked_list.indexOf(50)}")

    print()
    print("list item validation test: ")
    print("Does this list has item -1: ", linked_list.contains(-1))
    print("Does this list has item  0: ", linked_list.contains(0))
    print("Does this list has item 10: ", linked_list.contains(10))
    print("Does this list has item 20: ", linked_list.contains(20))
    print("Does this list has item 30: ", linked_list.contains(30))
    print("Does this list has item 40: ", linked_list.contains(40))
    print("Does this list has item 50: ", linked_list.contains(50))

    print()
    print("remove test: ")
    linked_list.removeFirst()
    linked_list.removeLast()
    linked_list.removeAt(1)

    print()
    print("list item print test: ")
    linked_list.print()

    print()
    print("Insert test: ")
    # should not print this item because it is negative index by negative feature not avaliable
    linked_list.insertAtIndex(-1, 0)
    linked_list.insertAtIndex(0, 0)
    linked_list.insertAtIndex(1, 15)
    # should be the last item because it is the same as the list length
    linked_list.insertAtIndex(4, 40)
    # should not print this item because greater than the list length
    linked_list.insertAtIndex(6, 152)
    linked_list.print()


def quick_test():
    list = LinkedList()
    list.insertFirst(10)
    arr = list.toArray()
    print(arr)
    print()
    print(f"List length is {list.size()}")
    time.sleep(1)
    print()

    list.insertLast(20)
    arr = list.toArray()
    print(arr)
    print()
    print(f"List length is {list.size()}")
    time.sleep(1)
    print()

    list.insertAtIndex(2, 30)
    arr = list.toArray()
    print(arr)
    print()
    print(f"List length is {list.size()}")
    time.sleep(1)
    print()

    list.insertAtIndex(0, 0)
    arr = list.toArray()
    print(arr)
    print()
    print(f"List length is {list.size()}")
    time.sleep(1)
    print()

    list.insertAtIndex(3, 25)
    arr = list.toArray()
    print(arr)
    print()
    print(f"List length is {list.size()}")
    time.sleep(1)
    print()

    list.insertAtIndex(5, 40)
    arr = list.toArray()
    print(arr)
    print()
    print(f"List length is {list.size()}")
    print()


if __name__ == "__main__":
    main()
