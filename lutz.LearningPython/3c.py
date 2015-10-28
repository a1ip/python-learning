class ThirdClass(SecondClass): 		# Наследует SecondClass
  def __init__(self, value): 		# Вызывается из ThirdClass(value)
    self.data = value
  def __add__(self, other): 		# Для выражения “self + other”
    return ThirdClass(self.data + other)
  def __str__(self): 			# Вызывается из print(self), str()
    return '[ThirdClass: %s]' % self.data
  def mul(self, other): 		# Изменяет сам объект: обычный метод
    self.data *= other
