menu = '''
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=>'''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:

    opcao = input(menu)

    if opcao == "d":
        deposito_valor = float(input("Informe o valor a ser depositado: "))
        if deposito_valor>0:
            saldo += deposito_valor
            extrato += f"Depósito: R$ {deposito_valor:.2f}\n"
        else:
            print("Informe um valor válido")
        
        

    elif opcao == "s":
        
        saque_valor = float(input("Informe o valor a ser sacado: "))
        
        sem_saldo = saque_valor > saldo
        excedeu_limite = saque_valor > limite
        excedeu_limite_saques = numero_saques >= LIMITE_SAQUES

        if sem_saldo:
            print("Operação falhou! Você não possui saldo suficiente")
        elif excedeu_limite:
            print(f"Operação falhou! Você ultrapassou o limite de saque de {limite}")
        elif excedeu_limite_saques:
            print("Operação falhou! Você não pode mais fazer saques hoje")
        else:
            if saque_valor>0:
                saldo -= saque_valor
                extrato += f"Saque: R$ {saque_valor:.2f}\n"
                numero_saques +=1
   

    elif opcao == "e":
        print("############EXTRATO BANCARIO############")
        print(extrato)
        print(f'Saldo: R$ {saldo:.2f}')

    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")