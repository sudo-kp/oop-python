class Node:
    def __init__(self, code, price):
        if not isinstance(code, int) or not isinstance(price, (int, float)):
            raise TypeError('Wrong product code or price.')
        if price<0:
            raise ValueError('Wrong price.')
        self.left = None
        self.right = None
        self.code = code
        self.price = price

    def __str__(self):
        return f'Product {self.code} costs {self.price} units.'


class BinaryTree:
    def __init__(self, root=None):
        if not isinstance(root, Node) and not root:
            raise TypeError('Wrong root.')
        self.root = root

    def search(self, code, current_node=None):
        if not isinstance(code, int):
            raise TypeError('Wrong search.')
        if not self.root:
            return None
        if not current_node:
            current_node = self.root
        if code == current_node.code:
            return current_node.price
        if code < current_node.code and current_node.left:
            return self.search(code, current_node.left)
        if code > current_node.code and current_node.right:
            return self.search(code, current_node.right)
        raise ValueError('No such product.')

    def insert(self, new_node, parent_node=None):
        if not isinstance(new_node, Node):
            raise TypeError('Wrong insertion.')
        if not self.root:
            self.root = new_node
        if not parent_node:
            parent_node = self.root
        if new_node.code == parent_node.code:
            raise ValueError('Duplicates of product codes.')
        if new_node.code < parent_node.code:
            if not parent_node.left:
                parent_node.left = new_node
            else:
                self.insert(new_node, parent_node.left)
        else:
            if not parent_node.right:
                parent_node.right = new_node
            else:
                self.insert(new_node, parent_node.right)

try:
    tree = BinaryTree(Node(1, 60))
    tree.insert(Node(2, 30))
    tree.insert(Node(-5, 20))
    tree.insert(Node(5, 40))
    a = tree.search(-5)
    print(a)
    code, quantity = input('Please enter the product code and quantity of products.\n').split()
    a = tree.search(int(code))
    print(a * int(quantity))
except TypeError as message:
    print(message)
except ValueError as message:
    print(message)
except:
    print('Error.')
