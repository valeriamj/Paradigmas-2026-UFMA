# Programa de classificação de notas

disciplinas = ["Algoritmos", "Redes", "Análise"]
notas = []
classificacoes = []

# Entrada das notas
for disciplina in disciplinas:
    while True:
        try:
            nota = float(input(f"Digite a nota de {disciplina}: "))

            if 0 <= nota <= 10:
                notas.append(nota)
                break
            else:
                print("A nota deve estar entre 0 e 10.")

        except ValueError:
            print("Digite apenas números.")

# Calcular a média
media = sum(notas) / len(notas)

# Gerar as classificações
for nota in notas:
    if nota >= 9.5:
        classificacao = "A"
    elif nota >= 8.0:
        classificacao = "B"
    elif nota >= 7.0:
        classificacao = "C"
    elif nota >= 6.0:
        classificacao = "D"
    else:
        classificacao = "E"

    classificacoes.append(classificacao)

# Mostrar resultados
print("\n====================================")
print("          RESULTADO FINAL")
print("====================================")

for i in range(len(disciplinas)):
    print(
        disciplinas[i],
        "- Nota:",
        notas[i],
        "- Classificação:",
        classificacoes[i]
    )

print("------------------------------------")
print(f"Média geral: {media:.2f}")

# Mostrar disciplinas com classificação D
print("\nDisciplinas com classificação D:")

encontrou_d = False

for i in range(len(disciplinas)):
    if classificacoes[i] == "D":
        print(disciplinas[i])
        encontrou_d = True

if not encontrou_d:
    print("Nenhuma disciplina recebeu D.")

print("====================================")
