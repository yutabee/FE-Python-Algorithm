from typing import Optional


class Node:
    def __init__(self, key: int):
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None
        self.key: int = key


def pre_order_traversal(node: Optional[Node]) -> None:  # 先行順探索
    if node:
        print(node.key, end=" ")
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)


def in_order_traversal(node: Optional[Node]) -> None:  # 中間順探索
    if node:
        in_order_traversal(node.left)
        print(node.key, end=" ")
        in_order_traversal(node.right)


def post_order_traversal(node: Optional[Node]) -> None:  # 後行順探索
    if node:
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        print(node.key, end=" ")

# 二分探索木の構築


def insert(node: Optional[Node], key: int) -> Node:
    if not node:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node


if __name__ == "__main__":
    # 木の構築
    keys = [30, 20, 40, 10, 25, 35, 50]
    root: Optional[Node] = None
    for key in keys:
        root = insert(root, key)

    # 探索の実行
    print("先行順探索:")
    pre_order_traversal(root)
    print("\n中間順探索:")
    in_order_traversal(root)
    print("\n後行順探索:")
    post_order_traversal(root)
