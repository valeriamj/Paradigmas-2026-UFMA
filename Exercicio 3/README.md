Valéria Marqus e Ster Thalita 

Pseudocódigo

INÍCIO

    Criar lista de disciplinas
    Criar lista de notas (vazia)
    Criar lista de classificações (vazia)
    media ← 0
    notasInseridas ← falso
    classificado ← falso

    ENQUANTO verdadeiro

        Mostrar menu:
            1 - Inserir notas
            2 - Calcular média e classificação
            3 - Mostrar resultados
            4 - Sair

        Ler opção

        ESCOLHA opção

            CASO 1:
                Limpar lista de notas
                Limpar lista de classificações
                classificado ← falso

                Para cada disciplina
                    REPETIR
                        Ler nota
                        SE nota < 0 OU nota > 10 ENTÃO
                            Mostrar "A nota deve estar entre 0 e 10"
                    ATÉ nota estar entre 0 e 10
                    Armazenar nota na lista
                Fim Para

                notasInseridas ← verdadeiro

            CASO 2:
                SE notasInseridas = falso ENTÃO
                    Mostrar "Insira as notas primeiro"
                SENÃO
                    media ← soma das notas / quantidade de notas
                    Limpar lista de classificações

                    Para cada nota
                        SE nota >= 9,5 ENTÃO classificação ← A
                        SENÃO SE nota >= 8,0 ENTÃO classificação ← B
                        SENÃO SE nota >= 7,0 ENTÃO classificação ← C
                        SENÃO SE nota >= 6,0 ENTÃO classificação ← D
                        SENÃO classificação ← E
                        FIM SE

                        Armazenar classificação na lista
                    Fim Para

                    classificado ← verdadeiro
                FIM SE

            CASO 3:
                SE classificado = falso ENTÃO
                    Mostrar "Calcule a média e classificação primeiro"
                SENÃO
                    Para cada disciplina
                        Mostrar disciplina, nota e classificação
                    Fim Para

                    Mostrar média

                    Mostrar as disciplinas que receberam D
                    (se nenhuma, mostrar "Nenhuma disciplina recebeu D")
                FIM SE

            CASO 4:
                Mostrar "Programa encerrado"
                INTERROMPER

            OUTRO CASO:
                Mostrar "Opção inválida"

        FIM ESCOLHA

    FIM ENQUANTO

FIM
