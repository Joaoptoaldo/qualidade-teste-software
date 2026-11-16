# Teste de Validação de Software

O **teste de validação** é a atividade que verifica se o software construído atende às necessidades reais do usuário e aos objetivos para os quais foi concebido. Em vez de perguntar se o código está correto em relação a uma especificação técnica, a validação pergunta se o produto certo foi construído.

---

## 1. Definição e Objetivo Central

A validação procura assegurar que o sistema atenda às **expectativas e necessidades do cliente** (Figueiredo, UFMG). O objetivo é responder à pergunta: *"Estamos construindo o produto correto?"* (Boehm, citado por Sommerville).

Enquanto a verificação pergunta *"Estamos construindo o produto corretamente?"* (aderência à especificação), a validação pergunta *"Estamos construindo o produto certo?"* (aderência à necessidade real).

Um sistema pode estar perfeitamente **verificado** (sem erros de implementação em relação à especificação) e, ainda assim, falhar na **validação** — se a especificação original não capturava o que o usuário realmente precisava.

---

## 2. Validação vs. Verificação

| Aspecto | Verificação | Validação |
|---|---|---|
| **Pergunta** | O produto foi construído corretamente? | Construímos o produto correto? |
| **Referência** | Especificação, documento de requisitos | Necessidade real do usuário, expectativa do cliente |
| **Ambiente** | Controlado, laboratório | Real ou simulado próximo do uso |
| **Momento** | Durante o desenvolvimento | Após a integração, antes da entrega |
| **Foco** | Componentes, conformidade com a especificação | Sistema completo, adequação ao uso |
| **Natureza** | Frequentemente estática (revisões, inspeções) | Dinâmica (execução do software) |

Fontes: Testsigma; Averna; Figueiredo (UFMG).

As duas atividades são complementares: a verificação alimenta a validação, e pular qualquer uma delas compromete a qualidade final.

---

## 3. Posição no Ciclo de Vida: O Modelo V

No **Modelo V**, a verificação ocorre no lado esquerdo (requisitos, projeto, codificação), enquanto a validação ocupa o lado direito, testando o produto já construído em direção à entrega.

```text
Requisitos ────────────────────────────── Teste de Aceitação (Validação)
   Projeto ──────────────────────── Teste de Sistema (Validação)
      Codificação ─── Teste de Integração (Verificação/Validação)
                   Teste de Unidade (Verificação)
```

O teste de validação surge **após a integração**, quando o software já existe como um todo executável.

---

## 4. Validação como Nível de Teste

Na estratégia clássica de testes (unidade → integração → sistema → validação/aceitação), a validação é o **último passo** antes da entrega, fornecendo a garantia final de que o software satisfaz os requisitos funcionais, comportamentais e de desempenho (Pressman).

A sequência típica é:

```text
Teste de Unidade         → verifica componentes isolados
Teste de Integração      → verifica interfaces entre componentes
Teste de Sistema         → verifica o sistema completo com hardware, BD, pessoas
Teste de Validação/Aceitação → verifica se o software atende ao usuário
```

.

---

## 5. Técnicas Aplicadas na Validação

A validação utiliza predominantemente técnicas de **caixa preta** (black-box), em que o foco está no comportamento observável — entradas e saídas — sem considerar a estrutura interna do código.

As técnicas mais comuns são:

- **Particionamento de Equivalência (ECP):** divide o domínio de entrada em classes válidas e inválidas; testa-se um representante de cada classe.
- **Análise de Valor Limite (BVA):** concentra casos de teste nos limites das classes de equivalência, onde erros são mais prováveis.
- **Tabelas de Decisão:** para combinações de condições e ações.
- **Teste Funcional:** casos derivados diretamente do documento de requisitos.

---

## 6. Critérios de Aceitação

A validação é orientada por **critérios de aceitação**, que definem as condições que o sistema deve satisfazer para ser formalmente aceito pelo usuário.

Um critério de aceitação bem escrito estabelece:

```text
DADO um contexto inicial
QUANDO uma ação é executada
ENTÃO um resultado observável deve ocorrer
```

A partir do critério, deriva-se o **caso de teste**, que especifica entradas, ações e resultados esperados.

---

## 7. Tipos de Validação: Alfa e Beta

A validação frequentemente se divide em duas abordagens complementares:

- **Teste Alfa:** realizado no **local do desenvolvedor**, com participação de usuários, usando dados gerais. Foco em identificar problemas funcionais antes de liberar externamente.
- **Teste Beta:** realizado no **local do usuário**, com dados reais, em ambiente operacional. Foco em validar o software sob condições reais de uso.

Ambos precedem o **Teste de Aceitação do Usuário (UAT)** formal, no qual o cliente certifica que o sistema está pronto para entrega ou implantação.

---

## 8. Automação da Validação

Frameworks como **Selenium**, **Cucumber** e **Robot Framework** permitem automatizar suítes de teste de aceitação, executando-as repetidamente à medida que o código evolui e integrando os critérios de aceitação a pipelines de entrega contínua.

A automação da validação é particularmente útil para **testes de regressão**, garantindo que funcionalidades validadas anteriormente continuem funcionando após alterações.

---

## 9. Considerações Finais

- A validação não substitui a verificação; ambas são necessárias para a qualidade.
- A validação depende de **requisitos e critérios de aceitação bem definidos** para produzir evidências úteis.
- Técnicas de caixa preta são a base da validação, mas a escolha de casos de teste exige julgamento sobre riscos e prioridades.
- Quando a validação é executada em diferentes ambientes (navegadores, sistemas operacionais, dispositivos), ela se aproxima do **teste de sistema**, ampliando o escopo para além da funcionalidade isolada.

> Em síntese: **validar é demonstrar, com evidências, que o software faz o que o usuário precisa — e não apenas o que a especificação diz.**