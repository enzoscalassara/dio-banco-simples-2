def menu():
    menu = """

    [s] Sacar
    [d] Depositar
    [e] Extrato
    [n] Nova Conta
    [c] Contas
    [u] Novo Usuário
    [x] Sair

    """
    return input(menu)

def depositar(*, saldo, extrato):
    print("Digite o valor a ser depositado:")
    valor = float(input())

    if valor > 0:
        extrato.append(f"R${valor:.2f} depositado")
        saldo += valor

        print(f"R${valor} foram depositados, novo saldo: {saldo}")

    else:
        print("Valor inválido")

    return saldo, extrato

def sacar(*, limite, saldo, saques, limite_saques, extrato):
    print("Digite o valor a ser sac"
          "ado:")
    valor = float(input())

    if 0 < valor < limite and valor <= saldo and saques < limite_saques:
        saldo -= valor
        print(f"R${valor} foi sacado, R${saldo} disponível.")
        saques += 1
        extrato.append(f"R${valor:.2f} sacado")


    else:
        print("Valor inválido")

    return saldo, saques, extrato

def print_extrato(*, extrato, saldo):
    print("EXTRATO".center(20, "#"))

    for elements in extrato:
        print(elements)

    print(f"Saldo atual: R${saldo:.2f}")

    print("EXTRATO".center(20, "#"))

def novo_usuario(*, usuarios):
    cpf = input("Digite seu cpf usando apenas numeros> \n")

    for i in usuarios:
        if usuarios["cpf"] == cpf:
            print("Este cpf já está cadastrado!")
            return

    nome = input("Nome:\n")
    data_nascimento = input("Data de nascimento:\n")
    endereco = input("Endereco:\n")

    usuarios.append({"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento, "endereco": endereco})
    print("Usuario foi criado")

def nova_conta(*, agencia, conta, usuarios):
    cpf = input("Digite seu cpf usando apenas numeros> \n")

    for i in usuarios:
        if i["cpf"] == cpf:

            print("conta criada")
            return {"agencia": agencia, "conta":conta, "usuario":i}

    return None

def ver_contas(contas):
    print("Contas".center(20, "#"))
    for conta in contas:
        print(f"Agencia: {conta['agencia']}\nConta: {conta['conta']}\nTitular: {conta['usuario']['nome']}")

    print("".center(26, "#"))

def main():
    LIMITE_SAQUES = 3
    LIMITE = 500
    AGENCIA = "0001"

    saldo = 0
    numero_saques = 0
    usuarios = []
    contas = []
    extrato = []

    while True:
        opcao = menu()

        if opcao == "d":
            saldo, extrato = depositar(saldo=saldo, extrato=extrato)

        elif opcao == "s":
            saldo, saques, extrato = sacar(limite=LIMITE, saldo=saldo, saques=numero_saques, limite_saques=LIMITE_SAQUES, extrato=extrato)

        elif opcao == "e":
            print_extrato(extrato=extrato, saldo=saldo)

        elif opcao == "x":
            break

        elif opcao == "n":
            conta = nova_conta(agencia=AGENCIA, conta=len(contas) + 1, usuarios=usuarios)
            if conta is None:
                print("Falha ao criar conta")

            else:
                contas.append(conta)


        elif opcao == "c":
            ver_contas(contas)

        elif opcao == "u":
            novo_usuario(usuarios=usuarios)


main()