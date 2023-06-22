Professor: [João Vicente Ferreira Lima](http://www.inf.ufsm.br/~jvlima)

Contato: jvlima em inf.ufsm.br ou CT/UFSM sala 380 Anexo B.

Carga horária: 60h.

Ementa oficial: https://www.ufsm.br/ementario/disciplinas/ELC1067

Horários: terças e quintas, 10:30 às 12:30.

**Página do corretor:** [https://joao-ufsm.github.io/l22023a/resultados/](./resultados/)

**Notas:** [Planilha](https://docs.google.com/spreadsheets/d/e/2PACX-1vSZtt6WyXJXVZ46iyxTPc1aE4SwI3sYI9AUXIyplJvbR7fNoU7pVu8Dzy9zr87lKPlfoZ7qPwqZpyBh/pubhtml) / [Planilha com comentário](https://docs.google.com/spreadsheets/d/1suV7uOAcGT1kit_gg4NscsgWGQ_n_m7w1ktIVWBT8rA/edit?usp=sharing) 

Calendário UFSM: https://www.ufsm.br/calendario/

## Sobre a disciplina

O objetivo da disciplina de Laboratório de Programação II é utilizar as principais estruturas de dados para solucionar problemas ligados à Computação.

## Métricas do relatório de código

- [Cyclomatic Complexity](https://docs.oclint.org/en/stable/rules/size.html#highcyclomaticcomplexity)
- [Análise Oclint](https://docs.oclint.org/en/stable/rules/index.html)
- [C++ Best Practices](https://github.com/cpp-best-practices/cppbestpractices/blob/master/00-Table_of_Contents.md)
- [C++ Core Guidelines](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines)
- [Google C++ Style Guide](https://google.github.io/styleguide/cppguide.html)
- Alternativas Valgrid - [Heaptrack](https://github.com/KDE/heaptrack), [Memoro](https://epfl-vlsc.github.io/memoro/), [Dr Memory](https://drmemory.org/)

## Material de apoio

- GDB [link 1](http://www.cs.umd.edu/~srhuang/teaching/cmsc212/gdb-tutorial-handout.pdf), [link 2](https://www.cs.cmu.edu/~gilpin/tutorial/), [link 3](http://www.lrc.ic.unicamp.br/~luciano/courses/mc202-2s2009/tutorial_gdb.txt). Ou a versão gráfica [DDD](https://www.gnu.org/software/ddd/)
- Valgrind [link 1](http://valgrind.org/docs/manual/quick-start.html), [link 2](https://web.stanford.edu/class/cs107/guide_valgrind.html)
- [GitHub Handbook](https://guides.github.com/introduction/git-handbook/)
- [Git Cheat Sheets](https://github.github.com/training-kit/)
- [Tech Talk: Linux Tolvards on Git](http://youtu.be/4XpnKHJAok8)
- [Introduction to Git with Scott Chacon of GitHub](https://youtu.be/ZDR433b0HJY)
- Cormen, Algoritmos: teoria e prática, 3o edição. ([notas 2008](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-spring-2008/lecture-notes/), [notas 2011](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/))
- Sedgewick, Algorithms, 4th edition. ([slides](http://algs4.cs.princeton.edu/lectures/))

## Trabalhos

| Prazo | Peso | Asssunto   |
|:---|----:|:------------------|
|  | `1,0` | [T8 - Dijkstra](./trabalhos/T8) |
| **13/07/2023** | `3,0` | [T7 - AVL Invaders com TDD](./trabalhos/T7) (parte 2) |
| **22/06/2023** | `3,0` | [T7 - AVL Invaders com TDD](./trabalhos/T7) (parte 1) |
| ~~**25/05/2023**~~ | `2,0` | [T6 - Árvore Binária de Busca](./trabalhos/T6)  |
| ~~**09/05/2023**~~ | `1,0` | [T5 - Logística de transporte](./trabalhos/T5) |
| ~~**02/05/2023**~~ | `2,0` | [T4 - Previdência Simplificada](./trabalhos/T4) |
| ~~**20/04/2023**~~ | `1,0` | [T3 - Cartas com lista](./trabalhos/T3) |
| ~~**13/04/2023**~~ | `1,0` | [T2 - Campo Minado](./trabalhos/T2) |
| ~~**05/04/2023**~~ | `1,0` | [T1 - Triângulos](./trabalhos/T1) |

## Aulas e trabalhos

|  # | Data             | Assunto          |
|---:|------------------|:-----------------|
|  1 | 2022-03-21 Ter | Apresentação da disciplina ([slides](https://docs.google.com/presentation/d/1TRYCyxJVxvltjvEDIneNl-2YCT2Ys2RNN4BRObkhfVE/edit?usp=sharing) e [vídeo](https://youtu.be/cUiFPopsXR4))   |
|  2 | 2022-03-23 Qui   | [Suporte no Windows para C++](./aulas/08_windows) |
|  3 | 2022-03-28 Ter   | [Introdução C++](./aulas/introducao_cxx) ([vídeo](https://youtu.be/pB-MdBKNpNo), [slides](./aulas/02_intro_cxx/02_intro_cxx.pdf)) |
|  4 | 2022-03-30 Qui   | **[T1](./trabalhos/T1)**, Alocação dinâmica de memória ([vídeo](https://youtu.be/KxvOkY4ipII), [slides](./aulas/03_memoria/03_memoria.pdf))  |
|  5 | 2022-04-04 Ter   | **[T2 - Campo Minado](./trabalhos/T2)** |
|  6 | 2022-04-06 Qui   | **[T2 - Campo Minado](./trabalhos/T2)** |
|  7 | 2022-04-11 Ter   | [Listas em C++](./aulas/09_listas) |
|  8 | 2022-04-13 Qui   | **[T3 - Cartas com lista](./trabalhos/T3)** |
|  9 | 2022-04-18 Ter   | **[T4 - Previdência Simplificada](./trabalhos/T4)** |
| 10 | 2022-04-20 Qui   | [Pilhas em C++](./aulas/13_pilhas) |
| 11 | 2022-04-25 Ter   | **[T5 - Logística de transporte](./trabalhos/T5)** |
| 12 | 2022-04-27 Qui   |  [Árvore binária de busca (ABB)](./aulas/16_abb/) |
| 13 | 2022-05-02 Ter   | **[T6 - Árvore Binária de Busca](./trabalhos/T6)** |
| 14 | 2022-05-04 Qui   | T6 |
| 15 | 2022-05-09 Ter   | T6 |
| 16 | 2022-05-11 Qui   | T6 |
| 17 | 2022-05-16 Ter   | [Árvores balanceadas (AVL)](./aulas/19_avl/) |
| 18 | 2022-05-18 Qui   | [Árvores balanceadas (AVL) - parte 2](./aulas/20_avl/) |
| 19 | 2022-05-23 Ter   | T6 |
| 20 | 2022-05-25 Qui   | **[T7 - AVL Invaders com TDD](./trabalhos/T7)** |
| 21 | 2022-05-30 Ter   | T7 |
| 22 | 2022-06-01 Qui   | T7 | 
| 23 | 2022-06-06 Ter   | T7 | 
| - | 2022-06-08 Qui   | **Feriado** (Corpus Christi)  |
| 24 | 2022-06-13 Ter   | T7 |
| 25 | 2022-06-15 Qui   | T7 |
| 26 | 2022-06-20 Ter   | [Containers e Algoritmos C++ STL](./aulas/20_algorithms) |
| 27 | 2022-06-22 Qui   |   T7 |
| 28 | 2022-06-27 Ter   | Grafos ([não-direcionados](./aulas/23_grafos/41UndirectedGraphs.pdf), [direcionados](./aulas/23_grafos/42DirectedGraphs.pdf))  |
| 29 | 2022-06-29 Qui   | Algoritmo de Dijkstra ([slides](aulas/23_grafos/44ShortestPaths.pdf), [demo](./aulas/23_grafos/44DemoDijkstra.pdf)) |
| 30 | 2022-07-13 Ter   | **[T7 - Prazo de apresentação](./trabalhos/T7)** |
|  | 2022-07-06 Qui     |  [Smart pointers](./aulas/11_pointers/) |
| - | 2022-07-11 Ter   | **Sem aula** (Sexta-feira)  |
| - | 2022-07-13 Qui   | **Sem aula** (Sábado)  |
| - | 2023-07-18 Ter | **Avaliações Finais** |

