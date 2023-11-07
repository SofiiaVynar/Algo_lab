class BinaryTree:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def Diameter(root: BinaryTree):
    def recursive(root):
        if root is None:
            return 0, 0

        left_depth, left_diameter = recursive(root.left)
        right_depth, right_diameter = recursive(root.right)

        if left_diameter >= right_diameter and left_diameter >= left_depth + right_depth:
            max_diameter = left_diameter
        elif right_diameter >= left_diameter and right_diameter >= left_depth + right_depth:
            max_diameter = right_diameter
        else:
            max_diameter = left_depth + right_depth

        depth = left_depth if left_depth >= right_depth else right_depth

        return depth + 1, max_diameter

    _, max_diameter = recursive(root)
    return max_diameter


if __name__ == '__main__':
    root = BinaryTree(1)
    root.left = BinaryTree(3)
    root.right = BinaryTree(2)
    root.left.left = BinaryTree(7)
    root.left.right = BinaryTree(4)
    root.left.right.right = BinaryTree(5)
    root.left.right.right.right = BinaryTree(6)
    root.left.left.left = BinaryTree(8)
    root.left.left.left.left = BinaryTree(9)

    print(Diameter(root))





