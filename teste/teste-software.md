# Teste de Software

Teste de software é o processo de avaliar um software para verificar se ele atende aos requisitos especificados, identificar defeitos e avaliar sua qualidade e seu comportamento em diferentes condições.

- **Objetivo:** encontrar falhas, defeitos e comportamentos incorretos antes que causem problemas aos usuários.
- **Elementos de um teste:** dados de entrada, pré-condições, passos de execução, resultados esperados e resultados obtidos.
- **Erro, defeito e falha:** erro é uma ação humana incorreta; defeito é um problema introduzido no software; falha é o comportamento incorreto observado durante a execução.

## Caso de Teste e Suíte de Testes

- **Caso de teste:** conjunto de condições, entradas, passos e resultados esperados usados para verificar um comportamento específico do software.
- **Suíte de testes:** conjunto organizado de casos de teste que verificam um sistema, componente ou funcionalidade.

## Técnicas de Teste

- **Caixa-preta:** testa o comportamento externo do software sem precisar conhecer sua implementação interna. Os testes são elaborados com base nos requisitos, nas entradas e nas saídas esperadas.
- **Caixa-branca:** considera a estrutura interna do software, incluindo código-fonte, decisões, caminhos de execução e fluxo de dados.
- **Teste funcional:** verifica se o software executa as funções e atende aos comportamentos especificados. Frequentemente utiliza técnicas de caixa-preta.

## Grafos

- **Grafo de fluxo de controle:** representa os possíveis caminhos de execução de um programa. Os nós representam instruções, blocos de código ou blocos básicos; as arestas representam as possíveis transferências de execução.
- **Análise de fluxo de dados:** estuda como os valores das variáveis são definidos, utilizados e propagados durante a execução. Pode ser realizada sobre o grafo de fluxo de controle.

## Complexidade Ciclomática

É uma métrica que mede a complexidade da estrutura de controle de um programa, indicando o número de caminhos linearmente independentes em seu grafo de fluxo de controle.

**Fórmula:**

\(M = E - N + 2P\)

- **M:** complexidade ciclomática.
- **E:** número de arestas do grafo.
- **N:** número de nós do grafo.
- **P:** número de componentes conectados do grafo.

Em um grafo de fluxo de controle com um único componente conectado, normalmente \(P = 1\). Nesse caso:

\(M = E - N + 2\)

A complexidade ciclomática também ajuda a estimar a quantidade mínima de caminhos linearmente independentes que precisam ser exercitados para obter cobertura de caminhos independentes.