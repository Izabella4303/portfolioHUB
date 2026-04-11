saldo = float(input("Digite o valor do Saldo: "))

continuar = True

while continuar:
    print("--- Caixa Eletrônico ---")
    print("Digite 1 para consultar saldo")
    print("Digite 2 para sacar valor")
    print("Digite 3 para depositar valor")
    print("Digite 4 para Sair")

    opcao = int(input("Escolha uma opção: "))
    if opcao == 1: 
        print ("O saldo atual é R$", saldo)

    elif opcao == 2:
        valor = 0
        valor = float(input("Digite o valor do saque: R$ "))
    
        if valor < saldo:
            saldo -= valor
            print ("Saque Concluido")
            print ("Saldo atual : R$", saldo)
        elif valor <= 0:
            print ("Valor invalido")

        else:
            print ("Saldo Insuficiente")

    elif opcao == 3:
        deposito = float(input("Digite o valor para deposito: R$ "))
        saldo += deposito
        print ("Saldo atual: R$ ", saldo)

    elif opcao ==4:
        print ("Saindo do Caixa Eletrônico")
        print ("--- Caixa Eletrônico ---")
        continuar = False

    else:
        print ("Opção inválida") 
