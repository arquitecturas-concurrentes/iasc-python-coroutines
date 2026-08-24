def cuenta_regresiva(numero):
    while numero > 0:
        yield numero
        numero -= 1

for numero in cuenta_regresiva(5):
    print(numero)

cuenta_regresiva(5)

# -----------------------------------

def fibonacci():
  a, b = 0, 1
  while True:
    c = yield a
    print(c)
    a, b = b, a+b

for numero in fibonacci():  # Utilización de generador como iterador
  print(numero)
