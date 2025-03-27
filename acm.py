class ACM:
  def __init__(self, money, machine):
    self._money = money
    self._machine = machine

  @property
  def money(self):
    return self._money

  @money.setter
  def money(self, value):
    self._money = value

  @property
  def machine(self):
    return self._machine

  @machine.setter
  def machine(self, value):
    self._machine = value

  def replace(self, money, machine):
    self.money = money
    self.machine = machine

  def money_after_sell(self):
    return self.money + self.machine.resale - self.machine.profit

  def machine_profit(self):
    return self.machine.profit

  def machine_resale(self):
    return self.machine.resale

