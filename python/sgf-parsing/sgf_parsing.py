class SgfTree:
    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
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

def _get_contents(string):
	pass

## EX: ;A[B];B[C]
def _tree_builder(tree, tree_contents):
	if tree_contents == "":
		return
	
	pass

# () == Trees
# ; == Nodes
## EX: (;A[B];B[C])
def parse(input_string):
    if input_string is None:
		_raise_empty_string()
	elif input_string == "()":
		_raise_tree_with_no_nodes()
	elif input_string == ";":
		_raise_node_without_tree()
		
	contents = _get_contents(input_string)

	return _tree_builder(SgfTree(), contents)
	