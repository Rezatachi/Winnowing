import libcst as cst


with open("moss.py") as f:
    contents = f.read()


class CodeVisitor(cst.CSTVisitor):
    def visit_Assign(self, node: cst.Assign) -> bool:
        print("--> NODE TREE: \n{}".format(node))
        print("--> CODE LINE FROM NODE TREE: \n{}".format(cst.parse_module("").code_for_node(node)))
        return True


demo = cst.parse_module(contents)
_ = demo.visit(CodeVisitor())
