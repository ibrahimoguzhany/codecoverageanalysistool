# ast_graph_visualizer.py
import ast
import networkx as nx
import matplotlib.pyplot as plt
from ast_node_visitor import ASTNodeVisitor

def build_ast_graph(code):
    visitor = ASTNodeVisitor()
    tree = ast.parse(code)
    visitor.visit(tree)
    return visitor.graph

def assign_colors_to_graph(graph, tested_lines):
    for node in graph.nodes:
        if hasattr(node, 'lineno'):
            graph.nodes[node]['color'] = 'green' if node.lineno in tested_lines else 'red'
        else:
            graph.nodes[node]['color'] = 'gray'
    return graph

def draw_graph(graph):
    colors = [graph.nodes[node]['color'] for node in graph.nodes]
    labels = {node: graph.nodes[node].get('label', str(node)) for node in graph.nodes}
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, labels=labels, node_color=colors, font_size=8, node_size=700)
    plt.show()
