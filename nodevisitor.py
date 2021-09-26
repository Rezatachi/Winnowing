import ast

# ast.NodeVistor is the primary tool for 'scanning' the tree. To use it, subclass it and ovveride methods visit_foo, coreresponding to the node classes.


class Navigator(ast.NodeVisitor):
    def __init__(self):
        self.data = []

    def visit_FunctionDef(self, node):

        node.name = "func"
        self.data.append(str(node.name))
        for i in range(len(node.args.args)):
            node.args.args[i].arg = "arg"
            self.data.append(str(node.args.args[i].arg))
        self.generic_visit(node)
        print("""PROGRAM ARRAY""")
        print(self.data)

    def visit_If(self, node: ast.If):
        node.test = "compare"
        self.data.append(node.test)

    def visit_For(self, node: ast.For):
        node.target.id = "loop"
        self.data.append(str(node.target.id))

    def visit_ClassDef(self, node: ast.ClassDef):
        node.name = "class"
        node.bases = "args"
        self.data.append(str(node.name))
        self.data.append(str(node.bases))

# Visit each node and print the target id's which are then converted into string

    def visit_Expr(self, node: ast.Expr):
        node.value.func.id = "call"
        node.value.func.args = "arg"
        self.data.append(str(node.value.func.id))
        self.data.append(str(node.value.func.args))

    def visit_Assign(self, node: ast.Assign):
        # Class 'str'
        node.targets[0].id = "var"
        self.data.append(str(node.targets[0].id))

        if hasattr(node.value, 'value'):
            node.value.value = "var"
            self.data.append(str(node.value.value))
        if hasattr(node, "value"):
            if node.value == ast.List:
                print("list")
