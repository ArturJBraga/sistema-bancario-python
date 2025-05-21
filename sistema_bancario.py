'''Este é um projeto que tem como objetivo desenvolver um sistema bancário utilizando a linguagem Python.
A medida que for tendo ideias de aperfeiçoamento irei atualizando o código aqui.
É importante salientar que parti de uma base já pronta e estou fazendo ajustes que julgo tornar o código 
melhor em algum aspecto'''

def menu():
    menu = """\n\n 
=========================== MENU ===========================
[d]\tDepositar \t\t\t[nu]\tNova Usuário
[s]\tSacar \t\t\t\t[nc]\tNovo conta
[e]\tExtrato \t\t\t[lc]\tListar contas
[q]\tSair 

Selecione=> """
    
    return input(menu).lower()

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n"+" Depósito realizado como sucesso! ".center(60, "_"))       
    else:
        print("\n"+" Operação falhou! O valor informado é inválido ".center(60, "!"))
        print("".center(60, "_"))
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n"+ " Operação falhou! você não tem saldo suficiente. ".center(60, "!"))
        print("".center(60, "_"))

    elif excedeu_limite:
        print("\n"+ " Operação falhou! O valor do saque excede o limite.".center(60, "!"))
        print("".center(60, "_"))

    elif excedeu_saques:
        print("\n"+ " Operação falhou! número máximo de saques excedido.".center(60, "!"))
        print("".center(60, "_"))

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n"+" Saque realizado com sucesso! ".center(60, "_"))

    else:
        print("\n"+" Operação falhou! O valor informado é inválido.".center(60, "!"))
        print("".center(60, "_"))

    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    print("\n"+" EXTRATO ".center(60, "="))
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\n Saldo:\t\tR$ {saldo:.2f}")
    print("".center(60, "="))

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n"+" Já existe usuário com esse CPF! ".center(60, "!"))
        print("".center(60, "_"))
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/UF): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print(" Usuário criado com sucesso! ".center(60, "_"))

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"]==cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n"+" Conta criada com sucesso! ".center(60, "_"))
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("\n"+" Usuário não encontrado, fluxo de criação encerrado! ".center(60, "!"))
    print("".center(60, "_"))

def listar_contas(contas):
    for conta in contas:
        linha = f"""
            Agência:\t{conta['agencia']}
            C/C:\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}"""
        print("".center(60, "_"))
        print(linha)
        print("".center(60, "_"))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            print("Operação finalizada".center(60, "_"))
            break

        else:
            print("\n"+" Operação inválida! Tente novamente ".center(60, "!"))
            print("".center(60, "_"))
        
main()       
