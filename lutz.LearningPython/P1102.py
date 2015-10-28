class tracer: # Состояние сохраняется в атрибутах экземпляра
  def __init__(self, func): # На этапе декорирования @
    self.calls = 0
    self.func = func # Cохраняет оригинальную функцию func
  def __call__(self, *args, **kwargs): # Вызывается при обращениях
    self.calls += 1 # к оригинальной функции
    print('call %s to %s' % (self.calls, self.func.__name__))
    return self.func(*args, **kwargs)

@tracer
def spam(a, b, c): # То же, что и spam = tracer(spam)
  print(a + b + c) # Вызывает метод tracer.__init__

@tracer
def eggs(x, y): # То же, что и eggs = tracer(eggs)
  print(x ** y) # Обертывает функцию eggs объектом tracer
