# Teste Estrutural e Teste em Ambiente Web

> Base: Pressman & Maxim (2021), caps. 19 e 21; Martins (2016), cap. 2.

---

## Parte I - Teste Estrutural (Caixa Branca)

### Conceito
- Deriva casos de teste da **estrutura interna** do código (lógica, decisões, ciclos, estruturas de dados).
- Objetivo: exercitar a implementação e revelar defeitos de lógica e fluxo; **complementa** o teste funcional.
- Requer: código-fonte, conhecimento das decisões/repetições, resultados esperados e um **critério de cobertura**.

### O que os testes devem exercitar
- Caminhos independentes do módulo
- Decisões lógicas (verdadeiro e falso)
- Ciclos nos limites e dentro das fronteiras
- Estruturas de dados internas

### Grafo de Fluxo de Controle (GFC)
| Elemento | Significado |
|---|---|
| **Nó** | bloco de comandos executados sequencialmente |
| **Aresta** | transferência de controle entre nós |
| **Região** | área delimitada por nós e arestas (a região externa também conta) |
| **Nó-predicado** | nó de decisão, com 2 ou mais arestas de saída |

### Caminho independente e conjunto-base
- Caminho independente: introduz **ao menos uma aresta/condição nova** em relação aos já considerados.
- O **conjunto-base** é formado por caminhos linearmente independentes; **não é único**.

### Complexidade ciclomática V(G)
Indica o número de caminhos independentes do conjunto-base (e a complexidade lógica).

| Forma | Fórmula |
|---|---|
| Regiões | `V(G) = R` |
| Arestas e nós | `V(G) = E − N + 2` |
| Nós-predicado | `V(G) = P + 1` |

### Teste de caminho básico
1. Construir o grafo de fluxo
2. Calcular V(G)
3. Determinar um conjunto-base
4. Projetar casos que executem cada caminho

### Exemplo: `calcularFrete(valor, premium)`
```java
double calcularFrete(double valor, boolean premium) {
    double frete = 20.0;
    if (valor >= 200) {
        frete = 0.0;
    } else if (premium) {
        frete = 10.0;
    }
    return frete;
}
```
- N = 6, E = 7, P = 2 → **V(G) = 3**
- Conjunto-base (nós: 2 = `valor>=200`, 3 = `frete=0`, 4 = `premium?`, 5 = `frete=10`):

| Caminho | Entrada | Saída |
|---|---|---|
| 1-2-3-6 | valor=250, premium=false | 0.0 |
| 1-2-4-5-6 | valor=100, premium=true | 10.0 |
| 1-2-4-6 | valor=100, premium=false | 20.0 |

### Critérios de cobertura (fluxo de controle)
| Critério | Exige | Observação |
|---|---|---|
| **Comandos / todos os nós** | cada comando executado ≥ 1 vez | 100% não garante que todas as decisões foram exercitadas |
| **Ramos / todas as arestas** | verdadeiro **e** falso de cada decisão | pode exigir mais casos que comandos |
| **Condição** | resultados relevantes de cada condição em predicados compostos | complementa a cobertura de ramos |

**Comandos ≠ ramos:** em `calcularFrete`, os testes `250/false` + `100/true` dão 100% de comandos, mas **não** 100% de ramos. Falta `100/false` (ramo `premium = false`).

### Teste baseado em fluxo de dados
Seleciona caminhos conforme **definições e usos** de variáveis.

| Sigla | Significado | Exemplo (`calcularFrete`) |
|---|---|---|
| **DEF** | valor é atribuído à variável | `frete = 20.0`, `frete = 0.0`, `frete = 10.0` |
| **C-USE** | uso computacional (expressão/saída) | `return frete` |
| **P-USE** | uso predicativo (decisão que afeta o fluxo) | `valor >= 200`, `premium` |

- Critério **"Todos os Usos"**: identificar ocorrências → classificar (def / c-use / p-use) → relacionar pares **d-u** → projetar casos que os exercitem.

### Teste de ciclos (loops)
- Foca na validade das construções de repetição; defeitos são frequentes nos **limites**.

**Ciclo simples** (n = máximo de passagens):
`0` (pular) · `1` · `2` · `m` (com m < n) · `n−1`, `n`, `n+1`

**Ciclos aninhados:**
1. Começar pelo ciclo mais interno, com os externos em valores mínimos
2. Aplicar os testes de ciclo simples no interno
3. Avançar para fora, mantendo os demais em valores típicos/mínimos
4. Repetir até cobrir todos os níveis

### O que a cobertura diz - e não diz
| Ajuda a | Não prova que |
|---|---|
| medir quais estruturas foram exercitadas | todos os defeitos foram encontrados |
| identificar lacunas no conjunto de testes | o software satisfaz todos os requisitos |
| comparar o conjunto com um critério explícito | outros dados/sequências não revelarão problemas |

### Atividades da parte estrutural
- **Atividade 1 — `classificar(n)`:** duas decisões → V(G) = 3. Casos: `n=-5` → −1; `n=4` → 2; `n=5` → 1.
- **Atividade 2 — `buscaBinaria`:** desenhar GFC, calcular V(G), definir conjunto-base e casos para cobrir todos os ramos.
- **Atividade 3 — `bubbleSort` (ciclos aninhados):** idem; aplicar também a estratégia de ciclos aninhados.

---

## Parte II - Teste em Ambiente Web

### Por que o contexto Web é específico?
- Opera em rede e interage com navegadores, servidores, bancos de dados e serviços.
- Conteúdo, interface e navegação são centrais para a experiência.
- Variações de configuração alteram o comportamento.
- Segurança e desempenho são riscos centrais.

### Sequência para testar uma WebApp (10 passos)
1. Revisar conteúdo
2. Revisar modelo de interface
3. Revisar modelo de navegação
4. Testar interação da interface
5. Testar componentes funcionais
6. Testar caminhos de navegação
7. Testar configurações
8. Testar segurança
9. Testar desempenho
10. Testar com usuários finais

### Focos de teste
| Foco | Objetivo | Exemplos de problemas / perguntas |
|---|---|---|
| **Conteúdo** | sintaxe, correção textual, exatidão e organização | informação desatualizada, link incorreto, imagem/legenda inconsistente |
| **Interface** | mecanismos de interação, estética, diferentes ambientes | formulário envia dados errados, comportamento difere entre navegadores, mensagem de erro pouco clara |
| **Navegação** | mecanismos e jornadas do usuário funcionam | todos os nós são alcançáveis? links/botões/retorno funcionam? caminhos alternativos levam ao resultado correto? |
| **Componente** | defeitos funcionais e integração (página, serviço, infraestrutura) | colaboração com outros componentes na arquitetura prevista |
| **Configuração** | compatibilidade (plataforma, navegador, hardware, servidor, protocolos) | usar **matriz de configurações**, priorizar combinações críticas, registrar ambiente/versão |
| **Segurança** | vulnerabilidades em cliente, rede e servidor | autenticação/autorização, entrada de dados e scripts maliciosos, comunicação cliente–servidor, acesso a dados protegidos |
| **Desempenho** | tempo de resposta sob carga, gargalos, recuperação | como o tempo varia com a carga? onde o sistema se torna inaceitável? recupera após picos? |

### Carga × esforço (stress)
- **Teste de carga:** comportamento sob condições de carga **definidas** (cenários esperados).
- **Teste de esforço (stress):** condições **extremas**, para observar degradação, falhas e recuperação.

### Caixa branca também na Web
- Teste unitário de serviços, controladores e funções de negócio.
- Cobertura de ramos e condições no código do servidor.
- Fluxo de dados em componentes que tratam entrada e persistência.
- Interface e navegação são mais orientadas ao comportamento externo (**caixa preta**); os dois tipos se combinam conforme o objetivo e o artefato.

### Atividade - WebApp de inscrição em evento acadêmico
Escolher 4 tipos de teste, descrever risco e caso de teste e indicar onde usar caixa preta e caixa branca. Exemplos:

| Tipo | Risco | Exemplo de teste |
|---|---|---|
| Navegação | usuário não conclui a submissão | percorrer cadastro → submissão → comprovante |
| Configuração | falha em navegador/versão | executar fluxo crítico em combinações priorizadas |
| Segurança | acesso indevido a trabalhos | acessar recurso sem autorização |
| Desempenho | degradação no prazo final | simular pico de usuários e medir resposta |

Caixa branca útil em: ramos dos serviços de autorização, regras de submissão e processamento de pagamento.

---

## Síntese
1. Caixa branca deriva testes da estrutura interna do software.
2. Grafo, caminhos independentes e V(G) apoiam o teste de caminho básico.
3. Cobertura é critério de adequação, **não prova de ausência de defeitos**.
4. Fluxo de controle, fluxo de dados e ciclos são perspectivas complementares.
5. Em WebApps, conteúdo, interface, navegação, configuração, segurança e desempenho ampliam o escopo do teste.

