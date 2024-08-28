estados = input().split()  # Estados do autômato
estado_inicial = input()  # Estado inicial
estados_aceitacao = input().split()  # Estado de aceitação (q0)
linguagem = input().split()  # Alfabeto

qtd_estados = len(estados)
transicoes = {}
for i in range(qtd_estados):
    linha = input().split()
    estado_atual = linha[0]
    transicoes[estado_atual] = {linguagem[0]: linha[1], linguagem[1]: linha[2]}

palavras = input().split()

for palavra in palavras:
    estado_atual = estado_inicial
    for letra in palavra:
        if estado_atual in transicoes and letra in transicoes[estado_atual]:
            estado_atual = transicoes[estado_atual][letra]
        else:
            estado_atual = None
            break

    if estado_atual in estados_aceitacao:
        print('aceita')
    else:
        print('rejeita')
