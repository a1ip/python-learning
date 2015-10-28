def rangetest(*argchecks): # Проверяет позиционные аргументы на вхождение
  print("argchecks=",argchecks)
  def onDecorator(func):   # в заданный диапазон
    if not __debug__:      # True – если “python -O main.py args...”
      return func          # Ничего не выполняет: просто возвращает
                           # оригинальную функцию
    else: # Иначе, на этапе отладки, возвращает обертку
      def onCall(*args):
        for (ix, low, high) in argchecks:
          print("ix=",ix,"low=",low,"high=",high,"args[ix]=",args[ix])
          if args[ix] < low or args[ix] > high:
            errmsg = 'Argument %s not in %s..%s' % (ix, low, high)
            raise TypeError(errmsg)
        return func(*args)
      return onCall
  return onDecorator
