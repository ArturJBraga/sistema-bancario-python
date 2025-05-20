'''Este é um projeto que tem como objetivo desenvolver um sistema bancário utilizando a linguagem Python.
A medida que for tendo ideias de aperfeiçoamento irei atualizando o código aqui.
É importante salientar que parti de uma base já pronta e estou fazendo ajustes que julgo tornar o código 
melhor em algum aspecto'''

def menu():
    menu = """\n\n 
=========================== MENU ===========================
[d] Depositar       [s] Sacar       [e] Extrato     [q] Sair 

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

        elif opcao == "q":
            print("Operação finalizada".center(60, "_"))
            break

        else:
            print("\n"+" Operação inválida! Tente novamente ".center(60, "!"))
            print("".center(60, "_"))
        
main()       
