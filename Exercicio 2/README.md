# Paradigmas-
Caixa Eletrônico em Python

Disciplina: [Paradigmas de Programação]

Professor: [Rondineli]

Alunos: Valéria Marques e Sther Thallyta

Descrição do programa

Este projeto apresenta um sistema de caixa eletrônico desenvolvido em Python. O programa permite consultar o saldo, realizar depósitos, efetuar saques e encerrar o sistema.

Pseudocódigo

INÍCIO

    // ==================================
    // ALGORITMO: Caixa eletrônico
    //===================================

    VARIAVEIS:
        saldo: REAL
        opcao: INTEIRO
        valor: REAL
        executando: BOOLEANO

    INICIO:
        // Inicialização das variáveis
        Saldo <- 1000.00
        executando <- VERDADEIRO

        ENQUANTO (executando == VERDADEIRO) FACA
            //Exibição do Menu de Opções
            ESCREVA("=======================")
            ESCREVA("   CAIXA ELETRÕNICO    ")
            ESCREVA("=======================")
            ESCREVA("1 - Consultar Saldo")
            ESCREVA("2 - Depositar")
            ESCREVA("3 - Sacar")
            ESCREVA("4 - Encerrar")
            ESCREVA("Escolha uma opção: ")
            LEIA(opcao)

            //Processamento da opção escolhida
            SE opcao == 1) ENTAO
                ESCREVA("Seu saldo atual é: R$ ", saldo)

            SENAO SE (opcao == 2) ENTAO
                ESCREVA("Digite o valor para depósito: R$ ")
                LEIA(valor)

                SE (valor > 0) ENTAO
                    saldo <- saldo + valor
                    ESCREVA("Depósito realizado com sucesso!")
                    ESCREVA("Novo saldo: R$ ", saldo)
                SENAO
                    ESCREVA("Valor inválido para depósito.")
                FIM_SE

            NAO SE (opcao == 3) ENTAO
                ESCREVA("Digite o valor para saque: R$ ")
                LEIA(valor)

            SE (valor <= 0) ENTAO
                ESCREVA("Valor inválido para saque.")
            SENAO SE (valor > saldo) ENTAO
                ESCREVA("Saldo insuficiente para esta operação.")
            SENAO
                saldo <- saldo - valor
                ESCREVA("Saque realizado com sucesso!")
                ESCREVA("Novo saldo: R$ ", saldo)
            FIM_SE

        SENAO SE (opcao == 4) ENTAO
            ESCREVA("Encerrando o sistema. Obrigado por utilizar!")
            executando <- FALSO // Altera a booleana para interromper o laço

        SENAO
            ESCREVA("Opção inválida! Tente novamente.")
        FIM_SE

        ESCREVA("") // Linha em branco para organizar a tela
    FIM_ENQUANTO

FIM

