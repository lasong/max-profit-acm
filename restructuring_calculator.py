
from acm import ACM

class RestructuringCalculator:
  def __init__(self, initial_capital, num_days, machines):
    self.initial_capital = initial_capital
    self.num_days = num_days
    machines.sort(key=lambda x: x.day)
    self.machines = machines

  def max_profit(self):
    state = [ACM(money=0, machine=None) for _ in range(self.num_days + 2)]
    state[0].money = self.initial_capital

    for day in range(self.num_days + 1):
      available_machines = self.__available_machines(day)

      if state[day].machine is None:
        # buy a machine
        for machine in available_machines:
          if state[day].money >= machine.price:
            state[day].replace(state[day].money - machine.price, machine)
      else:
        # attempt to sell the machine and buy a new one
        for machine in available_machines:
          if state[day].money_after_sell() >= machine.price and machine.profit > state[day].machine_profit():
            state[day].replace(state[day].money_after_sell() - machine.price, machine)

      # transfer money and machine to next day
      if state[day].machine is not None:
        state[day + 1].replace(state[day].money + state[day].machine_profit(), state[day].machine)
      else:
        state[day + 1].replace(state[day].money, None)

    result = state[self.num_days + 1].money
    if state[self.num_days + 1].machine is not None:
      result += state[self.num_days + 1].machine_resale()

    return result


  def __available_machines(self, day_index):
    return [m for m in self.machines if m.day == day_index + 1]

