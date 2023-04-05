
# T4 - Logística de transporte

## Deadline

Prazo: **03/05/2023 (Qua)** pelo link do GitHub (https://classroom.github.com/a/MFsOQnGV).

Você deve escolher seu nome na lista de alunos. Em seguida, o GitHub irá criar um repositório deste trabalho em seu usuário.

## Descrição

Uma transportadora armazena uma quantidade grande de caixas que eventualmente serão carregadas em um caminhão ou trem. As caixas são empilhadas no terminal de transporte assim que chegam.

Um caminhão pode carregar uma quantidade significativa de caixas. O tempo de carregar um caminhão depende do local das caixas de certa forma. Esse tempo aumenta quando as caixas não estão no topo das pilhas, mas só podem ser carregadas depois de retirar todas as outras caixas que estão acima.

O objetivo deste T4 é criar um plano para empilhar caixas de forma que maximize o tempo de carregamento no terminal da transportadora. O plano tem que permitir que cada caminhão seja carregado acessando apenas caixas do topo de uma pilha, além de minimizar o número de pilhas necessárias.

Sabemos a ordem que cada caminhão será carregado e ordem que cada caixa é recebida. Cada caminhão é representado por uma letra maiúscula entre A e Z e eles serão carregados em ordem alfabética. Cada caixa é marcada com a letra do caminhão destino. Vamos assumir que não há limite no tamanho das pilhas de caixas.

A entrada consiste em uma carga por linha com no máximo 50 caixas.
O programa fará a leitura do texto da entrada padrão (`std::cin`) e deve  imprimir o resultado na saída padrão (`std::cout`).
Um exemplo de entrada:
```
A
CBACBACBACBACBA
CCCCBBBBAAAA
ACMICPC
```
A saída do programa deve ter o número da carga e o número mínimo de pilhas usadas em cada linha:
```
Carga 1: 1
Carga 2: 3
Carga 3: 1
Carga 4: 4
```

Se preferir, pode testar com arquivos texto maiores de entrada utilizando o redirecionamento de entrada do programa com o comando abaixo:
```
$ ./t4 < exemplo.txt
```

## Dicas
- Cada pilha de caixas pode ser implementada usando `std::stack` ou `std::vector` como descrito na  [aula sobre pilhas](../../aulas/09_listas) em C++.

## Regras

- Usar somente C++!
- Use `std::stack` ou `std::vector`
- Não compila, zero.
- Plágio, zero.