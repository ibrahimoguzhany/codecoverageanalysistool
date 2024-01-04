# main.py
from cover_rate_calculator import analyze_code_and_calculate_cover_rate
from ast_graph_visualizer import build_ast_graph, assign_colors_to_graph, draw_graph

# Örnek Python kodu
test_code_full = """
import random

def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n - 1)

def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False

def generate_random_list(size, max_value):
    return [random.randint(1, max_value) for _ in range(size)]

def main():
    random_list = generate_random_list(5, 100)
    primes = [num for num in random_list if is_prime(num)]
    print(f"Random List: {random_list}")
    print(f"Prime Numbers: {primes}")

if __name__ == "__main__":
    main()
"""

# Test edilen fonksiyonları belirtelim
tested_functions = ['calculate_factorial', 'is_prime']

# Kod analizi ve cover rate hesaplama
analysis_results, cover_rate, function_lines = analyze_code_and_calculate_cover_rate(test_code_full, tested_functions)
for error in analysis_results:
    print(error)
print(f"Cover Rate: {cover_rate:.2f}%")

# AST grafiğini oluştur ve renklendir
ast_graph = build_ast_graph(test_code_full)
tested_lines = [line for func in tested_functions for line in range(*function_lines.get(func, (0, 0)))]
colored_graph = assign_colors_to_graph(ast_graph, tested_lines)

# Grafiği çiz
draw_graph(colored_graph)
