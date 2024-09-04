class AFND:
    def __init__(self, estados, simbolos, transicoes, estado_inicial, estados_finais):
        # Inicializa o autômato com seus estados, símbolos, transições, estado inicial e estados finais
        self.estados = estados
        self.simbolos = simbolos
        self.transicoes = transicoes
        self.estado_inicial = estado_inicial
        self.estados_finais = estados_finais

    def flat(self, lista):
        # Descompacta itens de uma lista que contêm múltiplos estados separados por vírgulas
        for i in range(0, len(lista)):
            if "," in lista[i]:
                itens = lista[i].split(",")
                lista[i:i+1] = itens  # Substitui o item por seus elementos separados
        return lista

    def processar_simbolo(self, estado_atual, simbolo):
        # Processa o símbolo atual e calcula os novos estados resultantes
        novos_estados = []
        for estado in estado_atual:
            for transicao in self.transicoes:
                # Se a transição é válida para o primeiro símbolo (self.simbolos[0]) e não é 'vazio'
                if transicao[0] == estado and simbolo == self.simbolos[0] and transicao[1] != 'vazio':
                    novos_estados.append(transicao[1])
                    novos_estados = self.flat(novos_estados)
                    novos_estados = self.adicionar_estados_por_transicao(novos_estados, transicao[1])
                # Se a transição é válida para o segundo símbolo (self.simbolos[1]) e não é 'vazio'
                elif transicao[0] == estado and simbolo == self.simbolos[1] and transicao[2] != 'vazio':
                    novos_estados.append(transicao[2])
                    novos_estados = self.flat(novos_estados)
                    novos_estados = self.adicionar_estados_por_transicao(novos_estados, transicao[2])
        return novos_estados

    def adicionar_estados_por_transicao(self, novos_estados, estado_adicionado):
        # Adiciona novos estados que podem ser alcançados a partir de um estado adicional
        for adicionado in estado_adicionado.split(","):
            for transicao2 in self.transicoes:
                if transicao2[0] == adicionado and transicao2[3] != 'vazio':
                    novos_estados.append(transicao2[3])
        return novos_estados

    def verificar_palavra(self, palavra):
        # Verifica se a palavra é aceita pelo autômato
        estado_atual = [self.estado_inicial] 
        if self.transicoes[0][3] != 'vazio':  
            estado_atual.append(self.transicoes[0][3])

        print(estado_atual)  

        for simbolo in palavra:
            print(simbolo)  # Exibe o símbolo atual
            estado_atual = self.processar_simbolo(estado_atual, simbolo)  # Calcula os novos estados
            print(estado_atual)  # Exibe os estados atuais após processar o símbolo

        # Verifica se algum dos estados atuais é um estado final
        for estado in estado_atual:
            if estado in self.estados_finais:
                return "aceita"  # A palavra é aceita se o estado final for alcançado
        return "rejeita"  # Caso contrário, a palavra é rejeitada

def ler_transicoes(estados):
    
    transicoes = []
    for i in range(len(estados)):
        transicoes.append(input().split())  
    return transicoes

def main():
    # Função principal que lê a entrada do usuário e executa o autômato
    estados = input("").split()  
    simbolos = input("").split() 
    estado_inicial = input("")  
    estados_finais = input("").split()  

    transicoes = ler_transicoes(estados)  
    palavra = input("")  

    
    afnd = AFND(estados, simbolos, transicoes, estado_inicial, estados_finais)
    resultado = afnd.verificar_palavra(palavra)

    print(resultado)  # Exibe o resultado final

if __name__ == '__main__':
    main()  # Executa a função principal se o script for executado diretamente
