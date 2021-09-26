import ast
from nodevisitor import Navigator
from pprint import pprint

# store class in var

# Open python file and read all the contents
with open("test.py") as f:
    contents = f.read()
# Parsing it and generating an object
tree = ast.parse(contents,  filename="test.py")
# Unparsing the parse which shows the tree's source code
# node = ast.dump(tree)
# # pprint(node)
e_tree = Navigator().visit(tree)
