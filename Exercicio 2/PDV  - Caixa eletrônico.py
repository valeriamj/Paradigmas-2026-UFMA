#Inicialização das variáveis
saldo = 1000.00
executando = True

#Laço principal de repetição
while executando:
    print("==================================")
    print("        CAIXA ELETRÔNICO          ")
    print("==================================")
    print("1 - Consultar Saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Encerrar")

    opcao = input("Escolha uma opção: ")

    #Processamento da opção escolhida
    if opcao == "1":
        print(f"\nSeu saldo atual é: R$ {saldo:.2f}")

    elif opcao == "2":
        valor = float(input("\nDigite o valor para depósito: R$ "))
        if valor > 0:
            saldo += valor
            print("Depósito realizado com sucesso!")
            print(f"Novo saldo: R$ {saldo:.2f}")
        else:
            print("Valor inválido para depósito.")
            
    elif opcao == "3":
        valor = float(input("\nDigite o valor para saque: R$ "))
        if valor <= 0:
            print("Valor inválido para saque.")
        elif valor > saldo:
            print("Saldo insuficiente para esta operação.")
        else:
            saldo -= valor
            print("Saque realizado com sucesso!")
            print(f"Novo saldo: R$ {saldo:.2f}")

    elif opcao == "4":
        print("\nEncerrando o sistema. Obrigado por utilizar!")
        executando = False #Altera a booleana para encerrar o while

    else:
        print("\nOpção inválida! Tente novamente.")

    print() # Linha em branco para organizar o console
    
