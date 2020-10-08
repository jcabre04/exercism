import re

class SgfTree:
    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        print(self.properties.items())
        print(other.properties.items())
        if not isinstance(other, SgfTree):
            return False
        for k, v in self.properties.items():
            if k not in other.properties:
                return False
            if other.properties[k] != v:
                return False
        for k in other.properties.keys():
            if k not in self.properties:
                return False
        if len(self.children) != len(other.children):
            return False
        for a, b in zip(self.children, other.children):
            if a != b:
                return False
        return True

    def __ne__(self, other):
        return not self == other


def _raise_empty_string():
    raise ValueError("Invalid String: Empty String")

def _raise_tree_with_no_nodes():
    raise ValueError("Invalid String: Tree with no nodes")
	
def _raise_node_without_tree():
    raise ValueError("Invalid String: Node without a tree")

def _raise_improperly_bound_tree():
    raise ValueError("Invalid String: A Tree is bound improperly by ()")

def _raise_no_delimiter():
    raise ValueError("Invalid String: Property has no delimiter")

def _raise_not_all_upper_property(key):
    raise ValueError("Invalid String: Property is not all uppercase: " + str(key))


def _process_single_tree(tree):
    tree = tree.replace("\\]","*")
    tree = tree.replace("\\[","&")

    temp_properties = {}
    if "[" not in tree:
        _raise_no_delimiter()

    key = tree[:tree.find("[")]
    if not key.isupper():
        _raise_not_all_upper_property(key)

    print(tree)

    values = []
    tree = tree[tree.find("["):]
    while tree:
        while tree and tree[0] == "[":
            val = tree[tree.find("[") + 1:tree.find("]")]

            val = "".join([char if char is not "*" else "]" for char in val])
            val = "".join([char if char is not "&" else "[" for char in val])

            values.append(val)
            tree = tree[tree.find("]") + 1:]
        temp_properties[key] = values
        if tree:
            key = tree[:tree.find("[")]
            if not key.isupper():
                _raise_not_all_upper_property(key)
            values = []
            tree = tree[tree.find("["):] 

    print(values)

    return temp_properties, tree

def _get_contents(string):
    properties = {}
    children = []

    if string[0] == "(" and string[-1] == ")":
        string = string.replace("(","").replace(")","")
        trees = string.split(";")
        trees = [tree for tree in trees if tree]

        print(trees)

        for tree in trees:
            if tree == "":
                break

            while tree:
                #process main tree, properties
                if not properties:
                    properties, tree = _process_single_tree(tree)
                else:
                    temp_properties = {}
                    temp_properties, tree = _process_single_tree(tree)
                    children.append(SgfTree(properties=temp_properties))
    else:
        _raise_improperly_bound_tree()

    return properties, children

def parse(input_string):
    if input_string is None or input_string == "":
        _raise_empty_string()
    elif input_string == "()":
        _raise_tree_with_no_nodes()
    elif input_string == ";":
        _raise_node_without_tree()

    properties, children = _get_contents(input_string)

    return SgfTree(properties=properties, children=children)
