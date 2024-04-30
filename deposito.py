import os
import time

def menu():
    return '==================================\n[d] Depositar\n[s] Sacar\n[e] Extrato\n[q] Sair\nDigite a função que deseja: '

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

nome = input( 'Insira o seu nome: ')
os.system('cls')
print( f'Bem-vindo(a), {nome}' )
time.sleep(1)
os.system('cls')

while True:

    opcao = input(menu())
    os.system('cls')

    if opcao == "d" or opcao == 'D':
        valor = float(input( 'Informe o valor do depósito: '))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print( f'Você depositou R$ {valor:.2f}' )
            input('Clique em qualquer tecla para continuar ')
            os.system('cls')

        else:
            print( 'Operação falhou! O valor informado é inválido.' )
            input('Clique em qualquer tecla para continuar ')
            os.system('cls')

    elif opcao == "s" or opcao == "S":
        valor = float(input( 'Informe o valor do saque: ' ))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print( 'Operação falhou! Você não tem saldo suficiente.' )
            input('Clique em qualquer tecla para continuar ')
            os.system('cls')

        elif excedeu_limite:
            print(' Operação falhou! O valor do saque excede o limite.' )
            input('Clique em qualquer tecla para continuar ')
            os.system('cls')

        elif excedeu_saques:
            print( 'Operação falhou! Número máximo de saques excedido.' )
            input('Clique em qualquer tecla para continuar ')
            os.system('cls')

        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saques += 1
            print( f'Você sacou R$ {valor:.2f}' )
            input('Clique em qualquer tecla para continuar ')
            os.system('cls')

        else:
            print( 'Operação falhou! O valor informado é inválido.' )
            input('Clique em qualquer tecla para continuar ')
            os.system('cls')

    elif opcao == "e" or opcao == "E":
        print( '\n================ EXTRATO ================' )
        print( 'Não foram realizadas movimentações.' if not extrato else extrato)
        print( f'\nSaldo: R$ {saldo:.2f}' )
        print( '==========================================' )
        input('Clique em qualquer tecla para continuar ')
        os.system('cls')

    elif opcao == "q" or opcao == "Q":
        print( 'Muito obrigado, tenha um bom dia' )
        print( 'Encerrando...')
        time.sleep(1)
        os.system('cls')
        break

    else:
        print( 'Operação inválida, por favor selecione novamente a operação desejada.' )
        input('Clique em qualquer tecla para continuar ')
        os.system('cls')