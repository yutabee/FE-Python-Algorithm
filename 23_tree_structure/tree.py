from typing import Optional


class TreeNode:
    def __init__(self, value: int):
        self.value: int = value
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None

    # insert a new node
    def insert(self, value: int) -> None:
        if value < self.value:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)

    # display the tree
    def display(self, level: int = 0) -> None:
        if self.left:
            self.left.display(level + 1)
        print(' ' * 4 * level + str(self.value))
        if self.right:
            self.right.display(level + 1)


if __name__ == '__main__':
    root = TreeNode(50)
    root.insert(20)
    root.insert(10)
    root.insert(30)
    root.insert(40)
    root.insert(60)
    root.insert(80)
    root.insert(70)
    root.insert(90)
    root.insert(110)
    root.display()
