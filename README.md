# Projeto: Cálculo de Idade com POO

## Descrição
Este projeto refatora um programa simples de cálculo de idade, originalmente desenvolvido com funções, utilizando o paradigma de Programação Orientada a Objetos (POO) em Python.

## Conceitos de POO utilizados
- **Classe:** `Pessoa`, que representa uma pessoa.
- **Atributos:** `nome` e `ano_nascimento`, que armazenam os dados da pessoa.
- **Métodos:** `calcular_idade()` realiza o cálculo da idade e `mostrar_resultado()` exibe o resultado.
- **Objeto:** no programa principal, é criado um objeto da classe `Pessoa` com os dados informados pelo usuário.

## Arquivos
- `main.py`: contém a classe `Pessoa` e o programa principal.
- `README.md`: apresenta a descrição e as instruções para executar o projeto.

## Requisitos
- Python 3 instalado.

## Como executar
1. Baixe ou extraia os arquivos do projeto.
2. Abra a pasta do projeto no VS Code, PyCharm ou outro editor.
3. Abra o terminal na pasta do projeto.
4. Execute:

```bash
python main.py
```

Se o comando `python` não funcionar no Windows, tente:

```bash
py main.py
```

## Exemplo de execução

```text
Digite o ano atual: 2026
Digite o seu ano de nascimento: 2003
Digite seu nome: Valéria

Resultado:
Olá, Valéria! Sua idade é:
23 anos
```

> Observação: o programa calcula a idade apenas pela diferença entre os anos. Para saber a idade exata, também seria necessário verificar se a pessoa já fez aniversário no ano atual.
