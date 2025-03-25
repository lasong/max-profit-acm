import sys

from input_reader import read_input
from restructuring_calculator import RestructuringCalculator

def main():
  if len(sys.argv) != 2:
    print("Usage: python main.py <input_file>")
    return

  file_path = sys.argv[1]
  test_cases = read_input(file_path)
  for case_num, (initial_capital, num_days, machines) in enumerate(test_cases, start=1):
    calculator = RestructuringCalculator(initial_capital, num_days, machines)
    result = calculator.max_profit()
    print(f"Case {case_num}: {result}")

if __name__ == "__main__":
  main()
