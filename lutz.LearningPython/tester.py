##tester func
"""
def tester(start):
 state = start # Обращение к нелокальным переменным
 def nested(label): # действует как обычно
  nonlocal state
  print(label, state) # Извлекает значение state из области
  state += 1
 return nested
"""
#tester class
"""
class tester: # Альтернативное решение на основе классов (Часть VI)
 def __init__(self, start): # Конструктор объекта,
  self.state = start # сохранение информации в новом объекте
 def nested(self, label):
  print(label, self.state) # Явное обращение к информации
  self.state += 1 # Изменения всегда допустимы
"""
#tester class as func
"""
class tester:
 def __init__(self, start):
  self.state = start
 def __call__(self, label): # Вызывается при вызове экземпляра
  print(label, self.state) # Благодаря этому отпадает
  self.state += 1
"""
#tester func as user func
def tester(start):
 def nested(label):
  print(label, nested.state) # nested – объемлющая область видимости
  nested.state += 1 # Изменит атрибут, а не значение имени nested
 nested.state = start # Инициализация после создания функции
 return nested
