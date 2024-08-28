def func_transicao(estado, num):
  d = {
      "q1": {0: "q1", 1: "q2"},
      "q2": {0: "q3", 1: "q2"},
      "q3": {0: "q2", 1: "q2"},
  }
  return d[estado].get(num, None)

estados = ["q1", "q2", "q3", "q4"]
inicial = "q1"
aceitacao = ["q2"]

sequencias = input().split()

for seq in sequencias:
  atual = inicial
  for num in seq:
      if num not in "01":
          atual = None
          print("caract. invalido")
          break
      atual = func_transicao(atual, int(num))


  if atual in aceitacao:
      print("aceita")
  else:
      if atual is not None:
          print("rejeita")
