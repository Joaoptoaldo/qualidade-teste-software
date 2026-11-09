# Primeiros Testes de Integração com Postman

Este resumo aborda a realização de testes de integração em uma API REST utilizando o projeto **Menu-Back-End** (desenvolvido em Java, Spring Boot, JPA, MySQL e Maven) e o **Postman**, explorando desde requisições básicas até a automação de fluxos CRUD completos.

---

## 1. O que é Teste de Integração?

Diferente de um teste unitário (que valida uma unidade isolada, como um `ProdutoService`), o **teste de integração** verifica se diferentes partes do sistema funcionam corretamente quando combinadas.

Ao enviar uma requisição pelo Postman, o fluxo percorre diversas camadas:

```text
Postman → HTTP → Spring Boot → Controller → JPA / Repository → MySQL

```

*Portanto, uma falha pode ocorrer em qualquer um desses pontos, e uma unidade isolada funcionando não garante integração bem-sucedida.*

---

## 2. Preparação do Projeto

1. **Clonar o repositório:**
```bash
git clone https://github.com/Herysson/Menu-Back-End.git

```


2. **Configurar o arquivo `src/main/resources/application.properties`:**
```properties
spring.datasource.url=jdbc:mysql://localhost:3306/menu?createDatabaseIfNotExist=true
spring.datasource.username=SEU_USUARIO
spring.datasource.password=SUA_SENHA

spring.jpa.hibernate.ddl-auto=update
spring.jpa.open-in-view=true
spring.jpa.show-sql=true
spring.jpa.properties.hibernate.format_sql=true

```


3. **Executar a aplicação:**
```bash
./mvnw spring-boot:run

```


*(No Windows: `mvnw.cmd spring-boot:run`)*. A API ficará disponível em `http://localhost:8080`.

---

## 3. Conceitos e Terminologia do Postman

* **Request / Response:** Requisição enviada e resposta recebida da API.
* **Collection:** Agrupamento de requisições relacionadas.
* **Environment & Variable:** Conjunto de valores reutilizáveis (ex: `baseUrl` ou `produtoId`).
* **Pre-request / Post-response script:** Códigos executados antes do envio ou após o recebimento da resposta, utilizando JavaScript.
* **Test:** Verificações automatizadas definidas com `pm.test()`.
* **Collection Runner:** Ferramenta para executar várias requisições e seus testes em sequência.

---

## 4. Criando e Automatizando Requisições (Fluxo CRUD)

### Exemplo de Script de Teste (Pós-resposta)

Para validar se a resposta foi bem-sucedida, se é JSON e se o corpo é uma lista:

```javascript
pm.test("A resposta deve indicar sucesso", function () {
    pm.response.to.be.success;
});

pm.test("A resposta deve ser JSON", function () {
    pm.response.to.be.json;
});

pm.test("O corpo da resposta deve ser uma lista", function () {
    const body = pm.response.json();
    pm.expect(body).to.be.an("array");
});

```

### Exemplo de Pré-requisição Dinâmica (`Pre-request`)

Para evitar duplicidade de nomes em cadastros repetidos:

```javascript
pm.environment.set(
    "nomeProdutoTeste",
    "Produto Teste " + Date.now()
);

```

### Exemplo de Armazenamento de ID no Pós-resposta

Para capturar o ID gerado e reutilizá-lo nas próximas requisições (`PUT`, `GET por ID`, `DELETE`):

```javascript
const body = pm.response.json();

if (body.id !== undefined && body.id !== null) {
    pm.environment.set("produtoId", body.id);
}

```

---

## 5. Integração Incremental e Regressão

* **Integração Incremental:** Consiste em adicionar novos componentes ou endpoints gradualmente (`GET` ➔ `POST` ➔ `GET por ID` ➔ `PUT` ➔ `DELETE`), testando a cada incremento.
* **Teste de Regressão:** Reexecução de testes anteriores para garantir que uma nova alteração não quebrou funcionalidades que já estavam funcionando. O **Collection Runner** do Postman é essencial para automatizar essa verificação em lote.

---

## 6. Checklist de Validação Prática

* [ ] Aplicação Spring Boot e MySQL rodando.
* [ ] Collection e Environment criados (`Menu - Local` com `baseUrl`).
* [ ] Endpoints do fluxo CRUD configurados (`GET`, `POST`, `PUT`, `DELETE`).
* [ ] Scripts de Pré-requisição e Pós-resposta aplicados.
* [ ] Execução automatizada validada com sucesso no **Collection Runner**.

## 7. Referências

- Projeto: [Menu-Back-End](<https://github.com/Herysson/Menu-Back-End?utm_source=chatgpt.com>).
- [Postman – Collections](<https://learning.postman.com/docs/collections/collections-overview/?utm_source=chatgpt.com>).
- [Postman – Environments e Variables](<https://learning.postman.com/docs/sending-requests/variables/managing-environments/?utm_source=chatgpt.com>).
- [Postman – Scripts](<https://learning.postman.com/docs/tests-and-scripts/write-scripts/intro-to-scripts/?utm_source=chatgpt.com>).
- [Postman – Test Scripts](<https://learning.postman.com/docs/tests-and-scripts/write-scripts/test-scripts/?utm_source=chatgpt.com>).
- [Postman – Collection Runner](<https://learning.postman.com/docs/collections/running-collections/intro-to-collection-runs/?utm_source=chatgpt.com>).

Bibliografia:

- PRESSMAN, Roger S.; MAXIM, Bruce R. Engenharia de software: uma abordagem profissional. 9. ed. Porto Alegre: AMGH, 2021.
- MARTINS, Marcos Danilo Chiodi. Testes de software. 1. ed. Rio de Janeiro: SESES, 2016.
  
