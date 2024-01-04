import unittest
from ..ast_graph_visualizer import build_ast_graph, assign_colors_to_graph

class TestASTGraphVisualization(unittest.TestCase):

    def test_ast_graph_creation(self):
        test_code = "def func():\n    pass"
        graph = build_ast_graph(test_code)
        self.assertTrue(len(graph.nodes) > 0)
        self.assertTrue(len(graph.edges) > 0)

    def test_graph_color_assignment(self):
        test_code = "def func():\n    pass\n\ndef another_func():\n    pass"
        graph = build_ast_graph(test_code)
        tested_lines = [1, 2]
        colored_graph = assign_colors_to_graph(graph, tested_lines)
        colors = [colored_graph.nodes[node]['color'] for node in colored_graph.nodes]
        self.assertIn('green', colors)
        self.assertIn('red', colors)

if __name__ == '__main__':
    unittest.main()
