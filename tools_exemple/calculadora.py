#!/usr/bin/env python3

import sys

"""
Calculadora de linha de comando (CLI) em Python.

Funções principais:
- Soma (-a), Subtração (-s), Multiplicação (-m), Divisão (-d)
- Verbose (-v) para mensagens explicativas
- Ajuda (-h) para ver o menu de uso

Exemplo:
    calculadora -m 2 14 3  -> 84.0

Observações:
- Todas as operações exigem pelo menos dois valores.
- Em divisão, nenhum divisor pode ser 0 (após o primeiro número).
"""

def help_menu():
    """Exibe o menu de ajuda com uso, opções e exemplos."""
    print(
"""
Uso :
    calculadora [opção] <valores> ...

    opções:
    -a somar todos os valores
    -s subtrair todos os valores
    -m multiplicar todos os valores
    -d dividir todos os valores
    -h mostra este menu de ajuda
    -v saída detalhada (verbose)

exemplos:
    calculadora -a 1 2 3
    calculadora -s 20 5 4
    calculadora -m 2 14 3 
    calculadora -d 100 5 2
    (todas as operações requerem dois ou mais valores)
"""
    )

def parse_numbers(args):
    """Converte a lista de strings em floats.

    Se algum valor não for numérico, mostra uma mensagem de erro
    e encerra a execução.
    """
    try:
        return [float(x) for x in args]
    except ValueError:
        print("Erro: todos os valores devem ser numeros")
        sys.exit(1)

def soma(valores):
    """Retorna a soma de todos os valores da lista."""
    return sum(valores)

def subtracao(valores):
    """Subtrai, em sequência, todos os valores a partir do primeiro.

    Ex.: [20, 5, 4] -> 20 - 5 - 4
    """
    resultado = valores[0]
    # Itera pelos valores restantes, subtraindo do acumulador
    for v in valores[1:]:
        resultado -= v
    return resultado

def multiplicacao(valores):
    """Multiplica todos os valores da lista sequencialmente."""
    resultado = 1
    # Começa em 1 para manter o produto correto
    for v in valores:
        resultado *= v
    return resultado

def divisao(valores):
    """Divide o primeiro valor pelos demais, em sequência.

    Ex.: [100, 5, 2] -> 100 / 5 / 2
    Se algum divisor for 0, encerra com erro.
    """
    resultado = valores[0]
    # Processa cada divisor restante
    for v in valores[1:]:
        if v == 0:
            print("Erro de divisão por 0")
            sys.exit(1)
        resultado /= v
    return resultado

def main():
    """Ponto de entrada da aplicação CLI.

    Faz o parsing dos argumentos, valida as entradas e executa a
    operação solicitada, imprimindo o resultado na saída padrão.
    """
    if len(sys.argv) < 2:
        help_menu()
        sys.exit(1)
    
    args = sys.argv[1:]

    verbose = False
    operacao = None
    valores= []

    # Varre os argumentos: flags (-v, -h, operação) e valores
    for arg in args:
        if arg == "-v":
            verbose = True
        elif arg == "-h":
            help_menu()
            sys.exit(0)
        elif arg in ("-a","-s","-m","-d"):
            operacao = arg
        else:
            valores.append(arg)

    if operacao is None:
        # Nenhuma operação reconhecida (-a, -s, -m, -d)
        print("Erro: nenhuma operação identificada")
        help_menu()
        sys.exit(1)
    
    if not valores:
        # Nenhum valor foi fornecido para processar
        print("Erro: nenhum valor informado")
        sys.exit(1)

    # Converte os valores de string para float, validando entradas
    numeros = parse_numbers(valores)

    if len(numeros) < 2:
        # Garante pelo menos dois números por operação
        print("Erro: informe pelo menos dois valores para a operação")
        sys.exit(1)

    # Executa a operação selecionada e imprime resultado
    if operacao == "-a":
        resultado = soma(numeros)
        if verbose:
            print(f"A soma dos valores é: {resultado}")
        else:
            print(resultado)

    elif operacao == "-s":
        resultado = subtracao(numeros)
        if verbose:
            print(f"A subtração dos valores é: {resultado}")
        else:
            print(resultado)

    elif operacao == "-m":
        resultado = multiplicacao(numeros)
        if verbose:
            print(f"A multiplicação dos valores é: {resultado}")
        else:
            print(resultado)
    elif operacao == "-d":
        resultado = divisao(numeros)
        if verbose:
            print(f"A divisão dos valores é: {resultado}")
        else:
            print(resultado)
    else:
        print(f"Opção inválida: {operacao}")
        help_menu()
        sys.exit(1)
    
if __name__ == "__main__":
    main()