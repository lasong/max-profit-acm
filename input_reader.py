def read_input(file_path):
  test_cases = []
  with open(file_path, 'r') as file:
    while True:
      line = file.readline().strip()
      if not line:
        break

      num_machines, initial_capital, num_days = map(int, line.split())
      if num_machines == 0 and initial_capital == 0 and num_days == 0:
        break  # Stop when we reach the termination case

      machines = []
      for _ in range(num_machines):
        line = file.readline().strip()
        day, price, resale, profit = map(int, line.split())
        machines.append((day, price, resale, profit))

      test_cases.append((initial_capital, num_days, machines))

  return test_cases

