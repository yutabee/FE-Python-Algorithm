from modules.linked_list import LinkedList


linked_list = LinkedList(5)
for i in range(10, 70, 10):
    linked_list.add(i)

linked_list.delete(10)
linked_list.display()
