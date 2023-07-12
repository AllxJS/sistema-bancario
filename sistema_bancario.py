saldo = 0
limite= 500
extrato = ""
numero_saque = 0
limite_saque = 3
    
while True:
    menu = input("\nMenu:\n[1] - Deposito\n[2] - Saque\n[3] - Extrato\n[4] - Sair\nDigite a opção desejada: ")
    
    if menu == "1":
        valor = float(input("\nDigite quanto deseja depositar: "))
        if valor > 0:
            saldo += valor
            extrato += f"\nDepósito: R$ {valor:.2f}"
        else:
            print("O valor informado é invalido!")
    elif menu == "2":
        valor = float(input("\nDigite quanto deseja sacar: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saque >= limite_saque
        if excedeu_saldo:
            print("Saldo insuficiente.")
        elif excedeu_limite:
            print("O valor do saque excede o limite.")       
        elif excedeu_saques:
            print("Numero maximo de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"\nSaque: R$ {valor:.2f}\n"
            numero_saque -= 1
        else:
            print("Ovalor informado é invalido.") 
    elif menu == "3":
       print("\n### Extrato ###\nNão foram realizadas operações" if not extrato else extrato)
       print(f"Saldo: R$ {saldo:.2f}")
    elif menu == "4":
        print("Programa Encerrado!\n")
        break
    else:
        print("Opção Incorreta, tente novamente!")


    
        
