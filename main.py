""" Utilize os seus conhecimentos em Python e crie um programa de finanças pessoais.

O programa deverá armazenar as informações em arquivos. O programa deverá:

Permitir informar as categorias dos gastos
Informar as entradas
Informar as saídas
Realizar relatórios (saldo do mês) """

import os
import time
from rich import print

if not os.path.exists("categorias.csv"):
    open("categorias.csv", "w").close()

with open("categorias.csv", encoding='UTF-8') as f:
    arquivo = f.read().split('\n')

while True:
    print("\n[bold orchid1]FINANÇAS PESSOAIS[/bold orchid1]")
    print('[1] Registrar entrada \n' 
    '[2] Registrar saida \n' 
    '[3] Emitir relatório total do mês \n'
    '[4] Emitir relatório de entradas \n'
    '[5] Emitir relatório de saidas \n'
    '[6] Sair')
    opcao = int(input('Digite o que você deseja fazer: '))
                      
    if opcao == 1:
        print('[bold green]Registro de entrada[/bold green]')
        categoria = input("Categoria: ")
        descricao = input("Descrição: ")
        valor = float(input("Valor: "))

        with open("categorias.csv", "a",  encoding="UTF-8") as f:
            f.write(f"\nEntrada;{categoria};{descricao};{valor}")
            
        print('[bold red]Entrada registrada![/bold red]') 
        print(f'Tipo: Saida')
        print(f'Categoria: {categoria}')
        print(f'Descrição: {descricao}')
        print(f'Valor: {valor}')
        time.sleep(4)

    elif opcao == 2:
        print('[bold green]Registro de saída[/bold green]')
        categoria = input("Categoria: ")
        descricao = input("Descrição: ")
        valor = float(input("Valor: "))

        with open("categorias.csv", "a") as f:
            f.write(f"\nSaida;{categoria};{descricao};{valor}")
        
        print('[bold green]Saida registrada!') 
        print(f'Tipo: Saida')
        print(f'Categoria: {categoria}')
        print(f'Descrição: {descricao}')
        print(f'Valor: {valor}')
        time.sleep(4)       

    elif opcao == 3:
        """ with open("categorias.csv", encoding='UTF-8') as f:
            arquivo = f.read().split('\n') """

        entradas = 0
        saidas = 0
        total = 0
        for c in range(0, len(arquivo)):
            arquivoPicotado = arquivo[c].split(';')
            print('-' * 50)
            print(f'Tipo: {arquivoPicotado[0]}')
            print(f'Categoria: {arquivoPicotado[1]}')
            print(f'Descrição: {arquivoPicotado[2]}')
            print(f'Valor: R${arquivoPicotado[3]}')
            
            if arquivoPicotado[0] == "Entrada":
                entradas += float(arquivoPicotado[3])
            else:
                saidas += float(arquivoPicotado[3])
            total += float(arquivoPicotado[3])
            time.sleep(1)

        print("\n[bold green]Resumo do Mês[/bold green]")
        print(f"Total de entradas: R${entradas}")
        print(f"Total de saidas: R${saidas}")
        print(f"Saldo: R${entradas-saidas}")
        print(f"Total: R${total}") 

        time.sleep(2.5)

    elif opcao == 4:
        entradas = 0
        for c in range(0, len(arquivo)):
            arquivoPicotado = arquivo[c].split(';')
            if arquivoPicotado[0] == 'Entrada':
                print('-' * 50)
                print(f'Tipo: {arquivoPicotado[0]}')
                print(f'Categoria: {arquivoPicotado[1]}')
                print(f'Descrição: {arquivoPicotado[2]}')
                print(f'Valor: R${arquivoPicotado[3]}')
                entradas += float(arquivoPicotado[3])
                time.sleep(1)
        print('-' * 50)
        print("\n[bold green]Resumo do Mês[/bold green]")
        print(f'Total de entradas: R${entradas}')
        time.sleep(1.5)

    elif opcao == 5:
        saida = 0
        for c in range(0, len(arquivo)):
            arquivoPicotado = arquivo[c].split(';')
            if arquivoPicotado[0] == 'Saida':
                print('-' * 50)
                print(f'Tipo: {arquivoPicotado[0]}')
                print(f'Categoria: {arquivoPicotado[1]}')
                print(f'Descrição: {arquivoPicotado[2]}')
                print(f'Valor: R${arquivoPicotado[3]}')
                saida += float(arquivoPicotado[3])
                time.sleep(1)

        print('-' * 50)
        print("\n[bold green]Resumo do Mês[/bold green]")
        print(f'Total de saidas: R${saida:.2f}')
        time.sleep(1.5)

    elif opcao == 6:
        break

    else:
        print("[bold red]Opção invalida[/bold red]")
        time.sleep(1)
    


  
    