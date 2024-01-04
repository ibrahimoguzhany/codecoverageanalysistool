import unittest
from ..cover_rate_calculator import analyze_code_and_calculate_cover_rate

class TestStaticCodeAnalysis(unittest.TestCase):

    def test_syntax_error_detection(self):
        test_code = "def func(x):\n    return x("
        errors, _, _ = analyze_code_and_calculate_cover_rate(test_code, [])
        self.assertTrue(any("Syntax Error" in error for error in errors))

    def test_style_issues_detection(self):
        test_code = "def func():\n    a = 1\n    b = 2\n    if a = b:\n        pass"
        errors, _, _ = analyze_code_and_calculate_cover_rate(test_code, [])
        self.assertTrue(any("Found '=' in a conditional statement" in error for error in errors))

    def test_cover_rate_calculation(self):
        test_code = "def func():\n    pass\n\ndef another_func():\n    pass"
        _, cover_rate, _ = analyze_code_and_calculate_cover_rate(test_code, ["func"])
        self.assertEqual(cover_rate, 50.0)

if __name__ == '__main__':
    unittest.main()
