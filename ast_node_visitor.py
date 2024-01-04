# ast_node_visitor.py
import ast
import networkx as nx

class ASTNodeVisitor(ast.NodeVisitor):
    def __init__(self):
        self.graph = nx.DiGraph()
        self.parent = None

    def visit(self, node):
        if not isinstance(node, ast.Module):
            self.graph.add_node(node, label=ast.dump(node, annotate_fields=False))
            if self.parent:
                self.graph.add_edge(self.parent, node)
        parent_backup = self.parent
        self.parent = node
        super().visit(node)
        self.parent = parent_backup
