# Calculadora CLI (pt-BR)

Uma calculadora de linha de comando simples em Python para somar, subtrair, multiplicar e dividir múltiplos valores.

Arquivo principal: [calculadora.py](calculadora.py)

## Requisitos
- Python 3

## Instalação
Baixe o arquivo `calculadora.py` e mova para a pasta `/usr/local/bin`:

```bash
sudo mv calculadora.py /usr/local/bin
sudo chmod +x /usr/local/bin/calculadora.py
```

Verifique se o arquivo está sendo encontrado:

```bash
which calculadora.py
# /usr/local/bin/calculadora.py
```

## Uso

```bash
calculadora [opção] <valor1> <valor2> <valor3> ...
```

### Opções disponíveis
- `-a`: somar todos os valores
- `-s`: subtrair todos os valores
- `-m`: multiplicar todos os valores
- `-d`: dividir todos os valores
- `-v`: saída detalhada (verbose)
- `-h`: mostra o menu de ajuda

### Observações
- Todas as operações requerem dois ou mais valores
- Em divisão, valores iguais a 0 após o primeiro causam erro

## Exemplos

### Soma
```bash
calculadora -a 1 2 3           # 6.0
calculadora -a -v 1 2 3        # A soma dos valores é: 6.0
```

### Subtração
```bash
calculadora -s 20 5 4          # 11.0
calculadora -s -v 20 5 4       # A subtração dos valores é: 11.0
```

### Multiplicação
```bash
calculadora -m 2 14 3          # 84.0
calculadora -m -v 2 14 3       # A multiplicação dos valores é: 84.0
```

### Divisão
```bash
calculadora -d 100 5 2         # 10.0
calculadora -d -v 100 5 2      # A divisão dos valores é: 10.0
```

### Ajuda
```bash
calculadora -h
```

## Mensagens de erro comuns

| Erro | Mensagem |
|------|----------|
| Valores não numéricos | `Erro: todos os valores devem ser numeros` |
| Nenhuma operação | `Erro: nenhuma operação identificada` |
| Nenhum valor | `Erro: nenhum valor informado` |
| Poucos valores | `Erro: informe pelo menos dois valores para a operação` |
| Divisão por zero | `Erro de divisão por 0` |

## Como o shell executa um comando no Linux

Quando você digita `calculadora -a -v 1 2 3`, acontece uma sequência de etapas:

1. **O shell lê e separa o comando** em nome (`calculadora`) e argumentos (`-a`, `-v`, `1`, `2`, `3`)
    - O shell tokeniza a entrada, respeitando espaços e caracteres especiais
    
2. **O shell procura o comando** na variável `PATH` (ex: `/usr/local/bin:/usr/bin:/bin`)
    - Percorre cada diretório listado em ordem até encontrar um arquivo executável com esse nome
    - Se não encontrar, retorna erro "command not found"
    
3. **O shell verifica permissões** do arquivo encontrado
    - Valida se o arquivo tem permissão de execução (`x`)
    - Lê o shebang (`#!/usr/bin/python3`) para determinar qual interpretador usar
    
4. **O kernel executa o programa** através da syscall `execve()`
    - Passa o caminho completo do programa, argumentos e variáveis de ambiente
    - Substitui o processo do shell pelo novo programa
    
5. **O programa recebe os argumentos** como lista de strings (`argv`)
    - Em Python: `sys.argv = ['calculadora.py', '-a', '-v', '1', '2', '3']`
    
6. **O programa interpreta os argumentos** e decide o que fazer
    - Processa flags, opções e valores conforme sua lógica
    
7. **O programa executa e exibe o resultado** na saída padrão (stdout)
    - Retorna um código de saída (exit code) ao shell

**Em resumo:** O shell localiza, valida permissões e executa o programa; toda a interpretação de argumentos é responsabilidade do próprio programa.
