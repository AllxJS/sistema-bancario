def deposito(saldo,valor,extrato):
    if valor > 0:
        saldo += valor
        extrato += f"\nDepósito: R$ {valor:.2f}"
        print("Deposito Realizado!")
    else:
        print("O valor informado é invalido!")
    return saldo,extrato

def saque(*,saldo, valor, extrato, limite, numero_saque,limite_saque):
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
        print("Saque Realizado!")
        
    else:
        print("O valor informado é invalido.") 
    
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("### Extrato ###\nNão foram realizadas operações" if not extrato else extrato)
    print(f"Saldo: R$ {saldo:.2f}")

def criar_usuario(usuarios):
    cpf = int(input("Informe CPF: "))
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("Ususario existente")
        return
    nome = input("Informe nome: ")
    data_nascimento = input("Informe a data de nascimento: ")
    endereco = input("Informe o endereço: ")
    
    print("Ususario cadastrado!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario ["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia,numero_conta, usuarios):
    cpf = input("Informe o CPF do usuario: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\nConta criada!")
        return{"agencia": agencia, "numero_conta": numero_conta, "usuario" : usuario}
    print("\nUsuario não encontrado!")

def listar_contas(contas):
    for conta in contas:
        print(f"Agencia:{conta['agencia']}\nNumero da conta: {conta['numro_conta']}\nTitular: {conta['usuario']['nome']}")

def main():     
    
    saldo = 0
    limite= 500
    extrato = ""
    numero_saque = 0
    limite_saque = 3
    AGENCIA = "0001"
    usuarios = []
    contas = []
    
    while True:
        menu = input("\nMenu:\n1 - Deposito\n2 - Saque\n3 - Extrato\n4 - Novo Usuario\n5 - Criar conta\n6 - Listar Contas\n7 - Sair\nDigite a opção desejada: ")
        
        if menu == "1":
            valor = float(input("\nDigite quanto deseja depositar: "))
            saldo,extrato = deposito(saldo,valor,extrato)
            
        elif menu == "2":
            valor = float(input("\nDigite quanto deseja sacar: "))
            saldo,extrato = saque(
                saldo  = saldo,
                valor = valor,
                extrato = extrato,
                limite= limite,
                numero_saque = numero_saque,
                limite_saque = limite_saque 
            )
            
        elif menu == "3":
            exibir_extrato(saldo, extrato = extrato)
            
        elif menu == "4":
            criar_usuario(usuarios)
        elif menu == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA,numero_conta,usuarios)

            if conta:
                contas.append(conta)                 
            
        elif menu == "6":
            listar_contas(contas)
        elif menu == "7":
            print("Programa Finalizado")
            break
        else:
            print("Opção Incorreta, tente novamente!")
   
main()