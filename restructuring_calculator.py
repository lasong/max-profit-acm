
class RestructuringCalculator:
  def __init__(self, initial_capital, num_days, machines):
    self.initial_capital = initial_capital
    self.num_days = num_days
    machines.sort()
    self.machines = [
      {
        'day': m[0],
        'price': m[1],
        'resale': m[2],
        'profit': m[3]
      } for m in machines]

  def max_profit(self):
    state = [{'money': 0, 'machine': None} for _ in range(self.num_days + 2)]
    state[0]['money'] = self.initial_capital

    for day in range(self.num_days + 1):
      available_machines = self.__available_machines(day)

      if state[day]['machine'] is None:
        # buy a machine
        for machine in available_machines:
          if state[day]['money'] >= machine['price']:
            self.__set_state(state, day, state[day]['money'] - machine['price'], machine)
      else:
        # attempt to sell the machine and buy a new one
        money_after_sell = state[day]['money'] + state[day]['machine']['resale'] - state[day]['machine']['profit']
        for machine in available_machines:
          if money_after_sell >= machine['price'] and machine['profit'] > state[day]['machine']['profit']:
            self.__set_state(state, day, money_after_sell - machine['price'], machine)

      # transfer money and machine to next day
      if state[day]['machine'] is not None:
        self.__set_state(state, day + 1, state[day]['money'] + state[day]['machine']['profit'], state[day]['machine'])
      else:
        self.__set_state(state, day + 1, state[day]['money'], None)

    result = state[self.num_days + 1]['money']
    if state[self.num_days + 1]['machine'] is not None:
      result += state[self.num_days + 1]['machine']['resale']

    return result


  def __available_machines(self, day):
    return [m for m in self.machines if m['day'] == day + 1]


  def __set_state(self, state, day, money, machine):
    state[day]['money'] = money
    state[day]['machine'] = machine
