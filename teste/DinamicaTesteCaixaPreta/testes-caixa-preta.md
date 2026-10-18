# Plano de testes - Caixa preta

Funcionalidade 1: percentual de horas extras (base de 40h por semana)

## O que o programa deve fazer

- Recebe as horas trabalhadas na semana
- Horas extras = horas - 40 (se for menos que 40, é 0)
- Percentual = horas extras / 40 x 100
- Avisa se passar de 25% (mais de 50h). Com 50h certinho não avisa.

## Casos de teste

| # | O que testa | Entrada | Esperado | Obtido | Passou? |
|---|-------------|---------|----------|--------|---------|
| 1 | Menos que 40h | 30 | 0 extras, 0%, sem aviso | 0,00 h; 0,00%; dentro do limite | Sim |
| 2 | Um pouco de extra | 45 | 5 extras, 12,5%, sem aviso | 5,00 h; 12,50%; dentro do limite | Sim |
| 3 | Muita extra | 60 | 20 extras, 50%, COM aviso | 20,00 h; 50,00%; alerta exibido | Sim |
| 4 | Limite: zero | 0 | 0 extras, 0%, sem aviso | 0,00 h; 0,00%; dentro do limite | Sim |
| 5 | Limite: 40h | 40 | 0 extras, 0%, sem aviso | 0,00 h; 0,00%; dentro do limite | Sim |
| 6 | Limite: 50h (25%) | 50 | 10 extras, 25%, sem aviso | 10,00 h; 25,00%; dentro do limite | Sim |
| 7 | Logo acima do limite | 50.1 | 10,1 extras, 25,25%, COM aviso | 10,10 h; 25,25%; alerta exibido | Sim |
| 8 | Máximo da semana | 168 | 128 extras, 320%, COM aviso | 128,00 h; 320,00%; alerta exibido | Sim |
| 9 | Passou de 168h | 169 | mensagem de erro | Entrada inválida: semana tem no máximo 168 horas | Sim |
| 10 | Número negativo | -5 | mensagem de erro | Entrada inválida: número de horas não pode ser negativo | Sim |
| 11 | Texto | abc | mensagem de erro, sem travar | Entrada inválida; conversão de 'abc' para número falhou | Sim |
| 12 | Vazio (só Enter) | (vazio) | mensagem de erro, sem travar | Entrada inválida; conversão de '' para número falhou | Sim |
| 13 | Decimal com ponto | 42.5 | 2,5 extras, 6,25% | 2,50 h; 6,25%; dentro do limite | Sim |
| 14 | Decimal com vírgula | 42,5 | aceita ou dá erro claro | Aceita; 2,50 h; 6,25%; dentro do limite | Sim |
| 15 | Símbolos | 4@0 | mensagem de erro | Entrada inválida; conversão de '4@0' para número falhou | Sim |

## Problemas encontrados

- Nenhum defeito funcional observado nos 15 casos executados.

## Resumo

- Total de testes: 15
- Passaram: 15
- Falharam: 0

Feedback geral: cálculos, limites, alerta acima de 25%, validações de faixa e formatos decimais corresponderam aos resultados esperados. As mensagens para texto vazio/não numérico são compreensíveis como erro, mas poderiam ser mais amigáveis e uniformes para o usuário final.

## Para a discussão

- A especificação não diz se o percentual é sobre 40h ou sobre o total trabalhado
- Também não diz se "mais que 25%" inclui os 25% exatos
- Se os dois grupos entenderam diferente, os testes 6 e 7 mostram isso
