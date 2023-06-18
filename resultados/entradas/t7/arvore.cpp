// arvore.cpp
// Estrutura de uma Árvore Binária de Busca (ABB) com balanceamento AVL.
//
// The MIT License (MIT)
//
// Copyright (c) 2023 João Vicente Ferreira Lima, UFSM
//
// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:
//
// The above copyright notice and this permission notice shall be included in
// all
// copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
// SOFTWARE.

#define CATCH_CONFIG_MAIN // O Catch fornece uma main()
#include "catch.hpp"

#include <list>

#include "abb.hpp"

TEST_CASE("Teste vazio") {
    Abb<int>* a;
    std::list<int> entrada {};
    a= abb_inicia(entrada);
    REQUIRE(abb_vazio(a) == true);
    abb_destroi(a);
}

TEST_CASE("Teste nao vazio") {
    Abb<int>* a;
    std::list<int> entrada {1};
    a= abb_inicia(entrada);
    REQUIRE(abb_vazio(a) == false);
    abb_destroi(a);
}


TEST_CASE("Caso 0") {
    Abb<int>* a;
    std::list<int> entrada {5, 3, 7};
    std::list<int> saida;
    std::list<int> resultado {5, 3, 7};
    a = abb_inicia(entrada);
    abb_preOrdem(a, saida);
    REQUIRE(saida == resultado);
    abb_destroi(a);
}

TEST_CASE("Caso ER") {
    Abb<int>* a;
    std::list<int> entrada {1, 2, 3};
    std::list<int> saida;
    std::list<int> resultado {2, 1, 3};
    a = abb_inicia(entrada);
    abb_preOrdem(a, saida);
    REQUIRE(saida == resultado);
    abb_destroi(a);
}

TEST_CASE("Caso DR") {
    Abb<int>* a;
    std::list<int> entrada {3, 2, 1};
    std::list<int> saida;
    std::list<int> resultado {2, 1, 3};
    a = abb_inicia(entrada);
    abb_preOrdem(a, saida);
    REQUIRE(saida == resultado);
    abb_destroi(a);
}

TEST_CASE("Caso DR-ER") {
    Abb<int>* a;
    std::list<int> entrada {5, 10, 7};
    std::list<int> saida;
    std::list<int> resultado {7, 5, 10};
    a = abb_inicia(entrada);
    abb_preOrdem(a, saida);
    REQUIRE(saida == resultado);
    abb_destroi(a);
}

TEST_CASE("Caso ER-DR") {
    Abb<int>* a;
    std::list<int> entrada {5, 1, 3};
    std::list<int> saida;
    std::list<int> resultado {3, 1, 5};
    a = abb_inicia(entrada);
    abb_preOrdem(a, saida);
    REQUIRE(saida == resultado);
    abb_destroi(a);
}

TEST_CASE("Caso DEL 0") {
    Abb<int>* a;
    std::list<int> entrada {5};
    a = abb_inicia(entrada);
    a = abb_remove( a, 5 );
    REQUIRE(abb_vazio(a) == true);
    abb_destroi(a);
}

TEST_CASE("Caso DEL 1") {
    Abb<int>* a;
    std::list<int> entrada {4, 2, 6, 7};
    std::list<int> saida;
    std::list<int> resultado {6, 4, 7};
    a = abb_inicia(entrada);
    a = abb_remove( a, 2 );
    abb_preOrdem(a, saida);
    REQUIRE(saida == resultado);
    abb_destroi(a);
}

TEST_CASE("Caso simples sequencial") {
    Abb<int>* a;
    std::list<int> entrada {1, 2, 3, 4, 5, 6, 7};
    std::list<int> saida;
    std::list<int> resultado {4, 2, 1, 3, 6, 5, 7};
    a = abb_inicia(entrada);
    abb_preOrdem(a, saida);
    REQUIRE(saida == resultado);
    abb_destroi(a);
}

TEST_CASE("Caso Notas MIT 2008") {
    Abb<int>* a;
    std::list<int> entrada {41, 20, 65, 11, 29, 50, 26, 23, 55};
    std::list<int> saida;
    std::list<int> resultado {41, 20, 11, 26, 23, 29, 55, 50, 65};
    a = abb_inicia(entrada);
    abb_preOrdem(a, saida);
    REQUIRE(saida == resultado);
    abb_destroi(a);
}

TEST_CASE("Caso N") {
    Abb<int>* a;
    std::list<int> entrada {50, 30, 24, 5, 28, 45, 98, 52, 60};
    std::list<int> saida;
    std::list<int> resultado {30, 24, 5, 28, 52, 50, 60};
    a = abb_inicia(entrada);
    a = abb_remove( a, 98 );
    a = abb_remove( a, 45 );
    abb_preOrdem(a, saida);
    REQUIRE(saida == resultado);
    abb_destroi(a);
}
