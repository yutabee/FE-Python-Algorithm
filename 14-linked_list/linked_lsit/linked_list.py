from typing import Optional


class Node:
    def __init__(self, data: str):
        self.data: str = data  # data
        self.next: Optional[Node] = None  # pointer to next node


class LinkedList:
    def __init__(self):
        self.head: Optional[Node] = None  # pointer to first node

    def append(self, data: str) -> None:
        new_node = Node(data)
        if not self.head:   # if list is empty
            self.head = new_node  # set head to new node
            return

        current = self.head  # current node
        while current.next:  # while there is a next node
            current = current.next  # move to next node
        current.next = new_node  # set next to new node

    def delete(self, data: str) -> None:
        if not self.head:  # if list is empty
            print("List is empty")
            return

        if self.head.data == data:  # if data is in list
            self.head = self.head.next  # delete first node
            return

        current = self.head  # current node
        while current.next:  # while there is a next node
            if current.next.data == data:  # if data is in next node
                current.next = current.next.next  # delete next node
                return
            current = current.next  # move to next node

    def display(self) -> None:
        current = self.head  # current node pointer
        while current:  # while there is a next node
            print(current.data, end=' -> ')  # print data
            current = current.next  # move to next node
        print("None")


if __name__ == "__main__":
    llist = LinkedList()
    llist.append("A")
    llist.display()
    llist.append("B")
    llist.display()
    llist.append("C")
    llist.append("D")
    llist.display()
    llist.append("E")
    llist.display()
    llist.append("F")
    llist.delete("A")
    llist.display()
    llist.append("G")
    llist.append("H")
    llist.append("I")
    llist.append("J")
    llist.append("K")
    llist.append("L")
    llist.append("M")
