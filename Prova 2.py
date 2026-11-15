class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self.nome = nome
        self.ano_nascimento = ano_nascimento

    def calcular_idade(self, ano_atual):
        return ano_atual - self.ano_nascimento

    def mostrar_resultado(self, idade):
        print("\\nResultado:")
        print(f"Olá, {self.nome}! Sua idade é:")
        print(f"{idade} anos")


def main():
    ano_atual = int(input("Digite o ano atual: "))
    ano_nascimento = int(input("Digite o seu ano de nascimento: "))
    nome = input("Digite seu nome: ")

    pessoa = Pessoa(nome, ano_nascimento)
    idade = pessoa.calcular_idade(ano_atual)
    pessoa.mostrar_resultado(idade)


if __name__ == "__main__":
    main()
