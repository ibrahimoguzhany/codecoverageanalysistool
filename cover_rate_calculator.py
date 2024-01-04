# cover_rate_calculator.py
import ast

def analyze_code_and_calculate_cover_rate(code, tested_functions):
    errors = []
    function_lines = {}
    all_imports = set()
    all_used_names = set()

    try:
        parsed_code = ast.parse(code)
    except SyntaxError as e:
        errors.append(f"Syntax Error: {e}")
        return errors, 0, function_lines

    for node in ast.walk(parsed_code):
        if isinstance(node, ast.Import):
            for name in node.names:
                all_imports.add(name.name)
        elif isinstance(node, ast.ImportFrom):
            for name in node.names:
                all_imports.add(name.name)
        if isinstance(node, ast.Name):
            all_used_names.add(node.id)
        if isinstance(node, ast.FunctionDef):
            start_line = node.lineno
            end_line = max(child.lineno for child in ast.walk(node) if hasattr(child, 'lineno'))
            function_lines[node.name] = (start_line, end_line)
            if not node.name.islower() or '-' in node.name:
                errors.append(f"Naming Convention Issue: Function '{node.name}' should be lowercase with underscores")
            if end_line - start_line > 10:
                errors.append(f"Code Quality Issue: Large function '{node.name}' detected (more than 10 lines)")

    unused_imports = all_imports - all_used_names
    for imp in unused_imports:
        errors.append(f"Style Issue: Unused import detected: '{imp}'")

    for node in ast.walk(parsed_code):
        if isinstance(node, ast.If) or isinstance(node, ast.While):
            if any(isinstance(child, ast.Assign) for child in ast.walk(node)):
                errors.append("Style Issue: Found '=' in a conditional statement. Did you mean '=='?")

    total_lines = len(code.splitlines())
    tested_lines = 0
    for func in tested_functions:
        if func in function_lines:
            start, end = function_lines[func]
            tested_lines += (end - start + 1)
    cover_rate = (tested_lines / total_lines) * 100 if total_lines > 0 else 0

    return errors, cover_rate, function_lines
