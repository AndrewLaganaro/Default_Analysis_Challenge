
<br></br>
## Contexto de negócio do exercício

- Contexto geral - A empresa X-Health atua no comércio B2B vendendo dispositivos eletrônicos voltados para saúde com amplo espectro de preços, e de variada sofisticação/complexidade. 
  
- Sobre as vendas - As vendas são feitas à crédito: o cliente B2B faz seu pedido e paga (à vista ou em várias parcelas, conforme o combinado pelo time de vendas) num tempo futuro pré-determinado.
  
- O problema - O time financeiro da X-Health tem observado um número indesejável de não-pagamentos ("default" ou calote, em bom português).

- O objetivo - Querem de alguma forma minimizar esse fenômeno. Desejam uma solução capaz de identificar os clientes podem vir o dar o default (ou "calote").

Antes de iniciar a solução, é fundamental estabelecer premissas que ajudarão a moldar sua abordagem. Isso inclui:

- Compreensão do Negócio: Entender profundamente o contexto no qual a X-Health opera, incluindo o perfil de seus clientes B2B, e como os processos de crédito e pagamento impactam a operação.

- Limitações e Desafios de Dados: Identificar quaisquer limitações nos dados fornecidos, como a representatividade, viés, ou qualidade dos dados. Considerar como esses fatores podem afetar a modelagem e a interpretação dos resultados.

- Aspectos Éticos e Regulatórios: Considerar quaisquer implicações éticas e regulatórias associadas ao uso de dados de crédito e pessoais, especialmente em relação à privacidade e discriminação.

- Impacto do Modelo: Refletir sobre como a implementação do modelo pode impactar a empresa e seus clientes. Isso inclui considerar tanto os benefícios potenciais quanto os riscos associados.


<br></br>
## Sobre o dataset

- Caminho: o dataset disponibilizado pela X-Health encontra-se em 
```
./_data/dataset_2021-5-26-10-14.csv
```
- Estrutura do .csv: para ler o arquivo, use  sep = '\t' e encoding = 'utf-8'.
- O dataset possui tanto variáveis internas (decorrentes do comportamento histórico do cliente B2B junto à X-Health), quanto variáveis externas consultadas em bureaus de crédito, como o Serasa.
- Cada linha do dataset representa um evento de compra de um conjunto de produtos, e tanto as variáveis internas quanto externas representam uma fotografia do cliente naquele instante.
- Valores faltantes estão indicados no dataset como "missing".
- Dicionário de dados:

| nome_coluna                    | desc                                                                                               |
| --------------------------     |----------------------------------------------------------------------------------------- |
| default\_3months               |Quantidade de default nos últimos 3 meses                                                          |
| ioi\_Xmonths                   |Intervalo médio entre pedidos (em dias) nos últimos X meses                                       |
| valor\_por\_vencer             |Total em pagamentos a vencer do cliente B2B, em Reais     |
| valor\_vencido                 |Total em pagamentos vencidos do cliente B2B, em Reais                                              |
| valor\_quitado                 |Total (em Reais) pago no histórico de compras do cliente B2B                |
| quant\_protestos               |Quantidade de protestos de títulos de pagamento apresentados no Serasa|
| valor\_protestos               |Valor total (em Reais) dos protestos de títulos de pagamento apresentados no Serasa|
| quant\_acao_judicial           |Quantidade de ações judiciais apresentadas pelo Serasa|
| acao\_judicial\_valor          |Valor total das ações judiciais (Serasa) |
| participacao\_falencia\_valor  |Valor total (em Reais) de falências apresentadas pelo Serasa |
| dividas\_vencidas\_valor       |Valor total de dívidas vencidas (Serasa)|
| dividas\_vencidas\_qtd         |Quantidade total de dívidas vencidas (Serasa)|
| falencia\_concordata\_qtd      |Quantidade de concordatas (Serasa)|
| tipo\_sociedade                |Tipo de sociedade do cliente B2B |
| opcao\_tributaria              |Opção tributária do cliente B2B |
| atividade\_principal           |Atividade principal do cliente B2B|
| forma\_pagamento               |Forma de pagamento combinada para o pedido |
| valor\_total\_pedido           |Valor total (em Reais) do pedido em questão|
| month                          |Mês do pedido|
| year                           |Ano do pedido|
| default                        |Status do pedido: default = 0 (pago em dia), default = 1 (pagamento não-realizado, calote concretizado)|
