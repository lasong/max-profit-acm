class Machine:
  def __init__(self, day, price, profit, resale):
    self._day = day
    self._price = price
    self._profit = profit
    self._resale = resale

  @property
  def day(self):
    return self._day

  @property
  def price(self):
    return self._price

  @property
  def profit(self):
    return self._profit

  @property
  def resale(self):
    return self._resale
