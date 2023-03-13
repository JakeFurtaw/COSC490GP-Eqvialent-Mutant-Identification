import networkx as nx
from pycparser import c_parser
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

# Create an empty graph
G = nx.DiGraph()

# Parse the C code and generate an AST
parser = c_parser.CParser()
ast = parser.parse('int main() { junk = addstr(DASH, dest, j, maxset); }')

# Traverse the AST and add nodes to the graph
def add_node(node):
    node_id = id(node)
    G.add_node(node_id, name=node.__class__.__name__)
    for _, child in node.children():
        child_id = id(child)
        G.add_node(child_id, name=child.__class__.__name__)
        G.add_edge(node_id, child_id)
        add_node(child)

add_node(ast)

# Draw the graph
nx.draw(G, with_labels=True)
plt.savefig("ast_graph.png")  # Save the graph as a PNG image
plt.show()  # Show the graph in a new window
plt.close
