# :key: Criptografia com Curvas Elípticas sobre Corpos Finitos
Trabalho 4 da disciplina de Criptografia, focado na aplicação de curvas elípticas sobre corpos finitos. O código é desenvolvido em Python e inclui funcionalidades-chave para operações em curvas elípticas, como verificação de pertencimento à curva, soma de pontos e cálculos envolvendo a aritmética modular.
## Funcionalidades Implementadas

### 1. Pertencimento à Curva

A função *`pertence_a_curva(P, Q, a, b, p)`* verifica se os pontos P e Q pertencem à curva elíptica representada pela equação ***y2=x3+ax+b mod p***. O resultado é exibido detalhadamente para cada ponto, indicando se pertencem à curva.

### 2. Soma de Pontos em Curvas Elípticas

A função *`soma_de_pontos(P, Q, a, b, p)`* realiza a soma de dois pontos P e Q na curva elíptica. São tratados casos especiais, como a soma com o ponto no infinito, garantindo a correta execução das operações.



