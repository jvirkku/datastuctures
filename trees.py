from graphviz import Digraph
from IPython.display import SVG

# #This data structure represents a tree, and in this case a family tree. Ancestor, parents and children can be added and the tree can be 
# visualized with Graphviz. Nodes can not be deleted due to the nature of this scenario (you dont want to delete people from family tree obviously).
# In this scenario there is always only one parent and children because everyone is divorced 


class Person: #initialized a node into the tree
    def __init__(self, name):
        self.name = name #name of a person
        self.children = []  # A family member can have multiple children

class FamilyTree:
    def __init__(self, root_name):
        self.root = Person(root_name) #when creating an istance of this class, it takes an ancestor as argument and now the ancestor is a root

    def add_child(self, parent_name, child_name):
        """ Add a child to a parent node in the family tree."""

        parent_node = self._find(self.root, parent_name) #find parent node with parent name that the children belongs to by recursively travelling through the tree
        if parent_node: #if parent is found -> add a child to the children list of that parent
            parent_node.children.append(Person(child_name))
        else:
            print(f"Parent '{parent_name}' not found in the tree.")

    def _find(self, current_person, wanted):
        """ Helper method to find a node by name."""

        if current_person.name == wanted: #current being the node in search, compared to the one we want to find
            return current_person
        # if the previous condition is false, so the current node is not the one we are looking for, we travel through the children of the current person
        for child in current_person.children: #loop through list of children and find specific child
            result = self._find(child, wanted) #using recursion we can travel through all children
            if result:
                return result
        return None


    def visualize(self):
        """Visualize the family tree using Graphviz."""

        dot = Digraph(comment='Family Tree')

        def add_nodes_edges(node):
            if node is None:
                return
            dot.node(node.name, node.name)  # Create a node for each family member
            for child in node.children:
                dot.edge(node.name, child.name)  # Create an edge between parent and child
                add_nodes_edges(child)

        add_nodes_edges(self.root)
        return SVG(dot.pipe(format='svg'))



# Initialize family tree with root ancestor
family_tree = FamilyTree("Grandparent Sally")

# Add children and grandchildren
family_tree.add_child("Grandparent Sally", "Lisa")
family_tree.add_child("Grandparent Sally", "Tim")
family_tree.add_child("Lisa", "Bob")
family_tree.add_child("Tim", "Sara")
family_tree.add_child("Tim", "Lara")


# Visualize the family tree (requires Graphviz installed)
family_tree.visualize()