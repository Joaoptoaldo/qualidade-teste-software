# Qualidade 

 - O que é qualidade?
    - 1) Conformidade com os requisitos 
            - subjetiva (depende do julgamento pessoal)
            - depende dos requisitos do usuário 

    - 2) Agregar valor
        - O que é agregar valor?
            - 1) Satisfazer o usuário
            - 2) Satisfazer o negócio

            
- Projeto:

        ---------------------------
        1) Comunicação (requisitos)
        ---------------------------
                    |
        -------------------------------------
        2) Planejamento (tempo, prazo, custo)
        -------------------------------------
                    |
        --------------------------------------------
        3) Projeto (desenho, arquitetura, modelagem)
        --------------------------------------------
                    |      
        -----------------------------------
        4) Construção (codificação, testes)
        -----------------------------------

    - A qualidade esta vinculada ao processo, ao padrão de desenvolvimento 


---

# Conceitos de Qualidade de Software

    - Dimensões de qualidade de Garvin
    - Fatores de qualidade de McCall
    - Fatores de qualidade ISO 9126
    - Fatores de qualidade desejados   
    - O Dilema da qualidade de software
    - Alcançando a Qualidade de Software

---

## Dimensões de qualidade de Garvin

Garvin propõe analisar a qualidade de um software de forma multidimensional, ou seja, considerando diferentes aspectos além de apenas “funcionar ou não”.

- Desempenho: verifica se o software entrega aquilo que foi especificado nos requisitos, atendendo às necessidades do usuário.

- Recursos: considera se o software possui funcionalidades adicionais que podem surpreender, facilitar o uso ou gerar maior satisfação ao usuário.

- Confiabilidade: avalia se o software funciona corretamente e sem falhas, estando disponível quando necessário e evitando erros durante o uso.

- Conformidade: verifica se o software segue padrões, normas e convenções de desenvolvimento, projeto e codificação.

- Durabilidade: analisa se o software pode ser modificado ou corrigido ao longo do tempo sem causar novos problemas ou reduzir sua confiabilidade.

- Facilidade de manutenção: verifica se é fácil e rápido corrigir erros ou realizar alterações, além de avaliar se os responsáveis possuem as informações necessárias para isso.

- Estética: está relacionada à aparência e à experiência visual do software. É uma dimensão subjetiva, pois cada usuário pode ter uma percepção diferente do que considera bonito ou agradável.

- Percepção: representa a qualidade percebida pelo usuário, que pode ser influenciada por experiências anteriores, opiniões e até preconceitos.

---

## Fatores de Qualidade de McCall

McCall, Richards e Walters propuseram uma forma de avaliar a qualidade de software dividindo os fatores em 3 grandes aspectos:

### 1. Operação do produto
Relacionada a como o software funciona durante o uso.

- Correção: o software faz o que foi solicitado?
- Confiabilidade: funciona sem falhas?
- Usabilidade: é fácil de aprender e utilizar?
- Integridade: protege os dados e controla o acesso?
- Eficiência: utiliza bem os recursos e apresenta bom desempenho?
  
### 2. Revisão do produto
Relacionada à facilidade de modificar, corrigir e testar o software.

- Facilidade de manutenção: é fácil corrigir e alterar?
- Flexibilidade: é fácil adaptar o software a novas necessidades?
- Testabilidade: é fácil testar e verificar se está funcionando corretamente?
  
### 3. Transição do produto
Relacionada à adaptação do software a outros ambientes e sistemas.

- Portabilidade: pode ser executado em diferentes plataformas?
- Reusabilidade: partes do software podem ser reutilizadas em outros projetos?
- Interoperabilidade: consegue trabalhar/comunicar-se com outros sistemas?
  
---

## Fatores de Qualidade ISO 9126

A ISO 9126 organiza a qualidade de software em 6 características principais, cada uma com seus próprios subatributos.

### 1. Funcionalidade
Verifica se o software atende às necessidades e funções esperadas.

- Adequabilidade: possui as funções necessárias?
- Exatidão: fornece resultados corretos?
- Interoperabilidade: consegue interagir com outros sistemas?
- Conformidade: segue normas e padrões?
- Segurança: protege dados e acessos?
  
### 2. Confiabilidade
Avalia se o software permanece funcionando corretamente durante o uso.

- Maturidade: apresenta poucas falhas?
- Tolerância a falhas: continua funcionando mesmo quando ocorre um problema?
- Facilidade de recuperação: consegue voltar ao funcionamento após uma falha?

### 3. Usabilidade
Avalia o quanto o software é fácil e agradável de utilizar.

- Facilidade de compreensão: o usuário entende como funciona?
- Facilidade de aprendizagem: é fácil aprender a usar?
- Operabilidade: é fácil operar e controlar?
  
### 4. Eficiência
Verifica se o software utiliza bem os recursos do sistema.

- Comportamento em relação ao tempo: responde rapidamente?
- Comportamento em relação aos recursos: utiliza adequadamente memória, processamento etc.?
  
### 5. Facilidade de manutenção
Avalia o quão fácil é corrigir, modificar e testar o software.

- Facilidade de análise: é fácil encontrar a causa de um problema?
- Facilidade de realização de mudanças: é fácil fazer alterações?
- Estabilidade: as mudanças não causam novos problemas?
- Testabilidade: é fácil testar o software?
  
### 6. Portabilidade
Verifica se o software pode ser levado para outro ambiente ou plataforma.

- Adaptabilidade: consegue se adaptar a diferentes ambientes?
- Facilidade de instalação: é fácil instalar?
- Conformidade: segue padrões de portabilidade?
- Facilidade de substituição: pode substituir outro software com facilidade?

---

## Fatores de Qualidade Desejados
Intuição: interface fácil de entender e usar, mesmo para iniciantes.

- Layout claro.
- Operações fáceis de localizar.
- Uso de metáforas conhecidas.

Eficiência: permite realizar tarefas de forma rápida e prática.

- Poucos cliques/movimentos.
- Informações fáceis de encontrar e compreender.
  
Robustez: capacidade de lidar com erros do usuário.

- Identifica entradas incorretas.
- Evita falhas do sistema.
- Orienta o usuário na correção.
  
### Visão Quantitativa
- Qualidade possui aspectos subjetivos, dificultando sua medição direta.
- Utilizam-se métricas de software para avaliar a qualidade.
- As métricas são indiretas → medem características que indicam a qualidade, não a qualidade em si.

---

## Dilema da Qualidade de Software
- Baixa qualidade: ninguém quer comprar → perda de clientes e mercado.
- Qualidade perfeita: exige muito tempo, esforço e dinheiro → pode levar à falência.
- Solução: buscar um equilíbrio entre:
    - Qualidade suficiente;
    - Tempo de desenvolvimento;
    - Custo de produção.
- Objetivo: criar um software bom o suficiente para atender ao mercado, sem buscar um perfeccionismo inviável.
- Resumo: Qualidade demais pode custar caro; qualidade de menos pode fazer o produto fracassar.

---

## Alcançando a Qualidade de Software
Qualidade não acontece por acaso: depende de um bom gerenciamento e de práticas consistentes de engenharia de software.

### Métodos de Engenharia
- Entender bem o problema.
- Criar um projeto adequado às necessidades.
- Considerar os fatores e dimensões de qualidade.
  
### Gerenciamento de Software
- Fazer estimativas realistas de prazo.
- Entender as dependências do cronograma.
- Evitar atalhos que prejudiquem a qualidade.
- Planejar e controlar riscos.
  
### Controle de Qualidade (CQ)
- Conjunto de ações para garantir que o software atinja as metas de qualidade.
- Revisar modelos e produtos para garantir completude e consistência.
  
### Garantia da Qualidade (GQ)
- Cria uma estrutura de suporte à qualidade.
- Envolve:
    - Engenharia de software;
    - Gerenciamento de projetos;
    - Controle de qualidade.
      
Resumo: Boa engenharia + bom gerenciamento + controle e garantia da qualidade = software de maior qualidade.


