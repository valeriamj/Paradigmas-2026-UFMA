# Função - entrada de dados
def entrada_dados():
    anoAtual = int(input("Digite o ano atual: "))
    anoNasc = int(input("Digite o seu ano de nascimento: "))
    nome = input("Digite seu nome: ")

    return anoAtual, anoNasc, nome


# Cálculo da idade
def calcular_idade(anoAtual, anoNasc):
    idade = anoAtual - anoNasc
    return idade


# Função - saída de dados
def mostrar_resultado(nome, idade):
    print("\nResultado:")
    print("Sua idade é:")
    print("Idade", idade, "anos")
