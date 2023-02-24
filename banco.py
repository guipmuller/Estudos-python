menu_banco = """
    ### BANCO ### 
    [1] Depósito
    [2] Saque
    [3] Extrato
    [0] Sair
    #############
    Digite a opção desejada: """

valor_em_conta = 0
extrato_total = "Movimentações na conta:\n"
saques_no_dia = int(0)
saque_maximo = 500
LIMITE_DIARIO_SAQUES = 3

while True:
    opcao = input(menu_banco)
    if opcao == "1":
        valor_deposito = float(input("Digite o valor a ser depositado R$ "))
        if (valor_deposito <= 0):
            print("Este valor não pode ser depositado")
        else:
            valor_em_conta = float(valor_em_conta + valor_deposito)
            print(f"Você depositou R${valor_deposito:.2f}.")
            print(f"Seu saldo atualizado é R${valor_em_conta:.2f}.")
            extrato_total = str(f"{extrato_total}+R${valor_deposito}\n")

    elif opcao == "2":
            valor_saque = float(input("Digite o valor a ser sacado R$ "))
            if valor_saque > saque_maximo:
                print("Erro na operação, o saque máximo é de R$500,00")
            elif valor_saque > valor_em_conta:
                print("Erro na operação, não há saldo suficiente em conta")
            elif saques_no_dia >= LIMITE_DIARIO_SAQUES:
                print("Erro na operação, o máximo de 3 operações de saque diárias atingido")
            elif valor_saque <= 0:
                print("Erro na operação, valor de saque inválido")
            else:
                saques_no_dia += 1
                valor_em_conta = float(valor_em_conta - valor_saque)
                print(f"Você sacou R${valor_saque:.2f}.")
                print(f"Seu saldo atualizado é R${valor_em_conta:.2f}.")
                extrato_total = str(f"{extrato_total}-R${valor_saque}\n")

    elif opcao == "3":
        print(f"\n#####################\n{extrato_total}\nO valor em conta é R${valor_em_conta:.2f}\n#####################")

    elif opcao == "0":
        print("Sessão encerrada")
        break

    else:
        print("Opção inválida.")