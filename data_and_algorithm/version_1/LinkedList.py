class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, data):
        self.data = data

    def setNext(self, next):
        self.next = next


class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        node = Node(item)
        node.setNext(self.head)
        self.head = node

    def search(self, data):
        temp = self.head
        while temp != None:
            if data == temp.getData():
                return True
            temp = temp.getNext()
        return False

    def remove(self, data):
        current = self.head
        previous = None
        while current != None:
            if data == current.getData():
                if previous == None:
                    previous = current.getNext()
                else:
                    previous.setNext(current.getNext())
                return True
            else:
                previous = current
                current = current.getNext()
        return False

    def __len__(self):
        temp = self.head
        count = 0
        while temp != None:
            count = count + 1
            temp = temp.getNext()
        return count

    def __iter__(self):
        temp = self.head
        while temp != None:
            yield temp.getData()
            temp = temp.getNext()

    def __getitem__(self, item):
        temp = self.head
        count = 0
        while temp != None:
            if count == item:
                return temp
            temp = temp.getNext()
            count = count + 1


class OrderedList(UnorderedList):
    def search(self, data):
        current = self.head
        while current != None:
            if current.getData() == data:
                return True
            elif current.getData() > data:
                return False
            else:
                current = current.getNext()

    def add(self, item):
        temp = Node(item)
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)
