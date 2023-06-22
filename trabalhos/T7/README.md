
# T7 - AVL Invaders com TDD

> Desbrave os perigos e trapaças das traiçoeiras árvores degeneradas. Organize os terríveis invasores com árvores balanceadas AVL e conquiste sua nota!


## Deadline

**Prazo TDD: 22/06/2022 (Qui)** pelo link do GitHub [https://classroom.github.com/a/mRF0kHMt](https://classroom.github.com/a/mRF0kHMt).

**Prazo Invaders (apresentação): 13/07/2022 (Qui)**

Se necessário, você deve escolher seu nome na lista de alunos. Em seguida, o GitHub irá criar um repositório deste trabalho em seu usuário.

**Não copie o repositório!** Na hora de criar o seu repostório de entrega, os arquivos estarão disponíveis.

## Descrição

Este trabalho consiste na implementação do jogo **Space Invaders**. Os invasores devem
ser organizados por uma representação de árvore binária de busca (ABB) balanceada AVL. A ABB terá movimentos para os lados e para baixo. Cada remoção resultará no re-balanceamento da árvore.
 
O jogo termina quando:
- Um invasor chegou no fim inferior tela, ou seja, perdeu o jogo.
- A árvore de invasores foi destruída, ganhando o jogo.

Os arquivos de exemplo, com o esqueleto do programa principal, estará disponível em seu repositório Git criado no arquivo `invaders.cpp`. 

O que deve ser feito no trabalho:
- **Invaders** - uma árvore ABB AVL deve armazenar os invasores. 
              Ela pode aumentar de tamanho e velocidade conforme
               a dificuldade aumenta. Também, quando ela chega nas
               extremidades horizontais ela retorna.
- **Laser** - o laser deve ser capaz de lançar vários tiros em sequencia
           usando uma lista (já suportado). 
- **Lógica de término do jogo** - desenvolver toda a lógica para ganhar
     ou perder o jogo podendo ter pontuação.
- **Manipulação da árvore** - ela deve crescer a cada nível que desce, e
  diminuir cada vez que um tiro atinge. Note que é preciso re-organizar após acerto.
- **Dificuldade** - em cada nível, a velocidade pode aumentar, assim como o tamanho com   valores aleatórios.

## Test Driven Development (TDD)

O [código-exemplo](https://github.com/jvlima-ufsm/tdd-invaders) do trabalho  usa o conceito de TDD (*Test Driven Development*) com o framework C++ [Catch2](https://github.com/catchorg/Catch2/tree/v2.x).
O framework Catch2 consegue ser utilizado apenas com o arquivo header `catch.hpp` sem necessidade de instalação.

**NÃO MODIFIQUE OS TESTES**, todos os testes estão prontos no arquivo `arvore.cpp`. A compilação e teste pode ser feita com os comandos:
```
$ g++ -Wall -std=c++11 arvore.cpp 
```

As funções que manipulam a struct de árvore `Abb` devem ser completadas. Note que a struct é um `template` podendo ser números, letras, ou qualquer outro tipo com suporte a comparação. Algumas funções já foram descritas para uso nos testes mas cada um podem (deve) adicionar mais funções a esta struct. As funções descritas são:
- `abb_inicia()` recebe uma lista de valores e retorna uma árvore AVL.
- `abb_insere()` insere um novo valor e retorna a raiz da AVL.
- `abb_remove()` remove o valor `v` e retorna a raiz da AVL.
- `abb_vazio()` testa se a árvore está vazia.
- `abb_preOrdem()` recebe uma lista vazia onde irá inserir os itens da árvore AVL em pré-ordem.
- `abb_esq_rotate()` efetua uma rotação à esquerda tendo `x` como pivô, retorna o nó `x`.
- `abb_dir_rotate()` efetua uma rotação à direita tendo `x` como pivô, retorna o nó `x`.
- `abb_destroi()` deve liberar a memória utilizada pela AVL.

Comentários sobre o exemplo:
- A execução irá mostrar o relatório de testes efetuados.
- Note que o programa não tem uma função `main()` porque não precisa! O Catch2 faz isso para nós.

## Avaliação do trabalho

Este trabalho terá **peso 3**. A nota será definida baseada na divisão abaixo:
- `0,4` para os testes de TDD.
- `0,6` para o jogo Invaders.

O relatório de análise estática de código será considerado na avaliação. Os erros terão **desconto** de:
- `0,5` se o código tem erros de prioridade 3, com tolerância para erros de `short variable name`.
- `1,0` para erros de prioridade 2.

## Allegro

Será necessário instalar a biblioteca Allegro versão 5
para gráficos. Em um sistema Ubuntu digite:
```
sudo apt install liballegro5-dev
```

No Windows, procure no site (https://www.allegro.cc). Algumas tutorias estão disponíveis em:
- https://www.youtube.com/watch?v=euK18wyK7go
- MinGW https://packages.msys2.org/package/mingw-w64-x86_64-allegro-static

Quem utilizar um
sistema Linux pode compilar com o programa `make` digitando:
```
make
```

## Dicas
- Procure materias sobre árvores ABB e AVL.
- Os testes são incrementais, ou seja, cada um deles aumenta a dificuldade.
- [MIT - Introduction to Algorithms (2020) - AVL Notes](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/resources/mit6_006s20_lec7/)
- [MIT - Introduction to Algorithms (2008) - AVL Trees](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2008/resources/lec4/)

## Regras

- Usar somente C++!
- Não compila, zero.
- Plágio, zero.