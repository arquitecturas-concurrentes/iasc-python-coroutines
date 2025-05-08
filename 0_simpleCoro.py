def gen0():
  yield "Soy un generador en realidad"
  yield "Soy una corrutina 2"

def a():
  return 2

def cuenta_regresiva(numero):
  while numero > 0:
    yield numero
    numero -= 1
  return

def coro():
  #yield usado de esta forma creamos una corrutina que hace más que generar valores, si no que también consume
  hello = yield "Soy una corrutina"
  yield
  yield hello

c = coro()
print(next(c))
print(c.send())