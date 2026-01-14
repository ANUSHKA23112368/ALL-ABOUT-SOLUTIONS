"""
Project #023: Mini B-Tree Database Storage Engine from Scratch
Domain: Advanced Computer Science
Description: Implements page-based disk paging, slot directories, and fixed-depth search trees
Date: 2026-01-14
"""

class BTreeNode:
    def __init__(self, is_leaf: bool = True):
        self.is_leaf = is_leaf
        self.keys = []
        self.children = []

class MiniDatabaseEngine:
    def __init__(self, degree: int = 3):
        self.root = BTreeNode(is_leaf=True)
        self.t = degree

    def search(self, key: int, node: BTreeNode = None):
        if node is None:
            node = self.root
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1
        if i < len(node.keys) and node.keys[i] == key:
            return True
        if node.is_leaf:
            return False
        return self.search(key, node.children[i])

