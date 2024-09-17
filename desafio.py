menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

# Variáveis globais
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def realizar_deposito(valor):
    """Realiza o depósito e atualiza o extrato."""
    global saldo, extrato
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("Operação falhou! O valor informado é inválido.")

def realizar_saque(valor):
    """Realiza o saque se as condições forem atendidas e atualiza o extrato."""
    global saldo, extrato, numero_saques
    if valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif valor > limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif numero_saques >= LIMITE_SAQUES:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("Operação falhou! O valor informado é inválido.")

def exibir_extrato():
    """Exibe o extrato e o saldo atual."""
    global extrato
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def main():
    """Função principal que executa o loop do menu."""
    while True:
        opcao = input(menu)
        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            realizar_deposito(valor)
        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            realizar_saque(valor)
        elif opcao == "e":
            exibir_extrato()
        elif opcao == "q":
            print("Saindo...")
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
