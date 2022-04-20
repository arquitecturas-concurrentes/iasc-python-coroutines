def coro():
  #yield usado de esta forma creamos una corrutina que hace más que generar valores, si no que también consume
  hello = yield "Soy una corrutina"
  yield hello

c = coro()
print(next(c))
print(c.send(", basada en generadores"))