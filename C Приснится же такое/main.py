

class Node:

    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def __repr__(self) -> str:
        return f"Node: {self.value}"
    

class Tree:

    def __init__(self, n) -> None:
        self.n = n
        self.root = Node(1)
        self.nodes = [Node(None), self.root]

        for i in range(2, self.n + 1):
            node = Node(i)
            parent = i // 2
            node.parent = self.nodes[parent]
            if self.nodes[parent].left is None:
                self.nodes[parent].left = node
            else:
                self.nodes[parent].right = node
            
            self.nodes.append(node)

    def swap_nodes(self, numb):
        v = self.nodes[numb]
        if self.root is v:
            return
        
        p = v.parent

        if p.parent is not None:
            pp = p.parent
            if pp.left is p:
                pp.left = v
            else:
                pp.right = v
            v.parent = pp
        else:
            self.root = v
            v.parent = None

        if v is p.left:
            v.left, p.left, p.parent = p, v.left, v
            if p.left:
                p.left.parent = p
        else:
            v.right, p.right, p.parent = p, v.right, v
            if p.right:
                p.right.parent = p


    def __in_order(self, node: Node):
        if node.left:
            self.__in_order(node.left)
        print(node.value, end=" ")
        if node.right:
            self.__in_order(node.right)

    def print_tree(self):
        self.__in_order(self.root)


n, _ = map(int, input().split(" "))

tree = Tree(n)

swaps = list(map(int, input().split(" ")))
for swap in swaps:
    tree.swap_nodes(swap)

tree.print_tree()
