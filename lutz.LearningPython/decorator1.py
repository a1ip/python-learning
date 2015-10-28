class tracer:
  def __init__(self, func): # На этапе декорирования @:
    self.calls = 0 # сохраняет оригинальную функцию func
    self.func = func
  def __call__(self, *args): # При последующих вызовах: вызывает
    self.calls += 1 # оригинальную функцию func
    print('call %s to %s' % (self.calls, self.func.__name__))
    self.func(*args)

@tracer
def spam(a, b, c): # spam = tracer(spam)
  print(a + b + c) # Обертывает функцию spam объектом декоратора
