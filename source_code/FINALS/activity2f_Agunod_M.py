class Node:
    __slots__ = ("value", "left", "right")

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return
        cur = self.root
        while True:
            if value < cur.value:
                if cur.left is None:
                    cur.left = Node(value); return
                cur = cur.left
            else:
                if cur.right is None:
                    cur.right = Node(value); return
                cur = cur.right

    def search(self, value):
        cur = self.root
        while cur and cur.value != value:
            cur = cur.left if value < cur.value else cur.right
        return cur is not None

    def inorder(self):
        res, stack, cur = [], [], self.root
        while stack or cur:
            while cur:
                stack.append(cur); cur = cur.left
            cur = stack.pop()
            res.append(cur.value)
            cur = cur.right
        return res

    def preorder(self):
        if not self.root:
            return []
        res, stack = [], [self.root]
        while stack:
            n = stack.pop()
            res.append(n.value)
            if n.right: stack.append(n.right)
            if n.left:  stack.append(n.left)
        return res

    def postorder(self):
        res = []
        self._post(self.root, res)
        return res

    def _post(self, n, res):
        if n:
            self._post(n.left, res)
            self._post(n.right, res)
            res.append(n.value)

    def delete(self, value):
        self.root, ok = self._del(self.root, value)
        return ok

    def _del(self, node, value):
        if node is None:
            return None, False
        if value < node.value:
            node.left, ok = self._del(node.left, value)
        elif value > node.value:
            node.right, ok = self._del(node.right, value)
        else:
            ok = True
            if node.left is None:
                return node.right, ok
            if node.right is None:
                return node.left, ok
            succ = self._min(node.right)
            node.value = succ.value
            node.right, _ = self._del(node.right, succ.value)
        return node, ok

    def _min(self, node):
        while node.left:
            node = node.left
        return node

    def count(self):
        n, stack, cur = 0, [], self.root
        while stack or cur:
            while cur:
                stack.append(cur); cur = cur.left
            cur = stack.pop()
            n += 1
            cur = cur.right
        return n

    def height(self):
        if not self.root:
            return -1
        h, stack = 0, [(self.root, 0)]
        while stack:
            n, d = stack.pop()
            if n:
                if d > h: h = d
                stack.append((n.left, d + 1))
                stack.append((n.right, d + 1))
        return h


def read_int(prompt):
    while True:
        s = input(prompt).strip()
        try:
            return int(s)
        except ValueError:
            print("Invalid input. Please enter an integer.")


def show(label, data):
    print(f"{label} TRAVERSAL:")
    print(" ".join(map(str, data)) if data else "Tree is empty.")


def main():
    bst = BinarySearchTree()
    while True:
        print("\nCAMPUS RESOURCE BST MANAGEMENT SYSTEM")
        print("=====================================")
        print("1. Insert a Resource ID")
        print("2. Delete a Resource ID")
        print("3. Search for a Resource ID")
        print("4. Display Inorder Traversal")
        print("5. Display Preorder Traversal")
        print("6. Display Postorder Traversal")
        print("7. Display Tree Information")
        print("8. Exit")
        print("=====================================")
        c = input("Enter your choice: ").strip()

        if c == "1":
            v = read_int("Enter Resource ID: ")
            bst.insert(v)
            print(f"Resource ID {v} inserted successfully.")
        elif c == "2":
            v = read_int("Enter Resource ID to delete: ")
            print(f"Resource ID {v} deleted successfully." if bst.delete(v)
                  else f"Resource ID {v} was not found.")
        elif c == "3":
            v = read_int("Enter Resource ID to search: ")
            print(f"Resource ID {v} was found in the tree." if bst.search(v)
                  else f"Resource ID {v} was not found.")
        elif c == "4":
            show("INORDER", bst.inorder())
        elif c == "5":
            show("PREORDER", bst.preorder())
        elif c == "6":
            show("POSTORDER", bst.postorder())
        elif c == "7":
            print("\nTREE INFORMATION")
            print(f"Root: {bst.root.value if bst.root else 'None'}")
            print(f"Total Nodes: {bst.count()}")
            print(f"Tree Height: {bst.height()}")
        elif c == "8":
            print("\nThank you. Program terminated.")
            break
        else:
            print("Invalid choice. Please select 1-8.")


if __name__ == "__main__":
    main()



