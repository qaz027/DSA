class BSTNode:
    def preorder(self, visited):
        current = self
        if current.val is not None:
            visited.append(current.val)
        if current.left:
            current.left.preorder(visited)
        if current.right:
            current.right.preorder(visited)
        return visited

    # don't touch below this line

    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)
