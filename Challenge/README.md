## Instruções gerais
- O presente repositório é de caráter pessoal e privado, não podendo ser compartilhado pelo candidato por quaisquer meios.
- A solução do exercício deverá ser elaborada única e exclusivamente pelo candidato, sem ajuda **pessoal** externa. Obviamente, não há problemas em caso de consultas em livros ou meios eletrônicos.
- O exercício em questão é fictício e não é parte de qualquer projeto real desenvolvido ou em desenvolvimento pela YYY.
- O exercício tem caráter classificatório, e não eliminatório. Portanto, caso tenha algum problema e não consiga resolver todo o exercício, envie a solução até onde conseguiu evoluir.
- A solução deverá ser entregue num repositório à parte, conforme descrito na seção "Sobre a entrega do exercício" abaixo.
- O prazo típico para entrega do exercício é de 1 semana. Mas caso haja algum problema no meio do caminho, nos comunique e combinamos um novo prazo, sem maiores problemas.
- **Não se preocupe caso não obtenha métricas excepcionais no seu modelo: faça seu melhor, mas esse não será o aspecto central a ser analisado, mas sim sua capacidade de análise, raciocínio, qualidade de código e organização/documentação**.  


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



<br></br>
## Expectativas do exercício:
1 - Um Jupyter Notebook com uma **análise exploratória** dos dados do dataset disponibilizado. Use sua criatividade e nos mostre os insights que encontrar.

2 - Um Jupyter Notebook com todo o **pipeline de estruturação do modelo probabilístico de inferência de default**: desde a limpeza e/ou transformação dos dados (se necessário), até o treinamento do modelo de aprendizado de máquina e avaliação de resultados. O candidato pode escolher a solução que julgar ser o melhor para o problema.

3 - Um Jupyter Notebook apenas para sua **função de predição**: é esperada uma função que irá receber novos dados (em forma de dicionário) e retornar a predição de default. 

Exemplo: se no seu modelo final optou por usar as variáveis preditoras "ioi\_3months", "valor\_vencido" e "valor\_total\_pedido", espera-se que sua função de predição tenha como input um dicionário da forma
```
input_dict = {"ioi_3months": 3, "valor_vencido":125000, "valor_total_pedido":35000}
```
onde os valores no dicionário acima são os hipotéticos novos valores, e retorne um dicionário com o valor da predição:

```
{"default":0}
```
ou 

```
{"default":1}
```

4 - Preparar uma apresentação dos resultados e insights obtidos, destinada a um público de negócios. A apresentação deve comunicar eficazmente as descobertas técnicas de forma compreensível para não especialistas em ML/AI. Aqui estao alguns pontos a serem abordados na apresentação:

   - Uma visão geral do problema e da abordagem adotada.
   - Principais insights da análise exploratória de dados.
   - Detalhes sobre o modelo desenvolvido ou solucao de dados, incluindo a escolha, justificativa e desempenho.
   - Discussão sobre as implicações de negócios dos resultados, incluindo como eles podem impactar a tomada de decisão na X-Health.
   - Recomendações práticas baseadas nas conclusões do modelo.
   - Reflexões sobre limitações, riscos potenciais e considerações éticas.
   - Formato: A apresentação pode ser em formato PowerPoint ou similar, com uma duração sugerida de 20-30 minutos.

Além disso, a apresentação deve incluir a descrição de cenários potenciais para a implementação bem-sucedida do modelo. Esses cenários ajudarão a ilustrar como a solução pode ser efetivamente integrada às operações da empresa, destacando os possíveis caminhos e estratégias:

- Cenário de Implementação - Descreva um cenário hipotético, mas realista, de como o modelo seria implementado na prática. Isso deve incluir detalhes sobre a integração do modelo nos sistemas existentes da X-Health, como ele seria usado nas decisões de crédito, e quaisquer mudanças operacionais necessárias.

- Plano de Avaliação: Elabore um plano para avaliar a eficácia do modelo no cenário proposto. Isso deve incluir métricas específicas de desempenho, métodos para testar o modelo em condições realistas, e um cronograma para revisão e ajustes contínuos.

- Considerações de Manutenção e Escalabilidade: Discuta como o modelo será mantido e atualizado ao longo do tempo, e como ele pode ser escalado ou adaptado para atender às mudanças nas necessidades do negócio ou no ambiente de mercado.

- Riscos e Mitigações: Identifique potenciais riscos associados à implementação do modelo, incluindo erros de previsão, viés do modelo, e dependência excessiva na automação. Propor estratégias para mitigar esses riscos.

*Lembrete*: É crucial equilibrar os aspectos técnicos e de negócios na apresentação. Embora a precisão técnica seja importante, a capacidade de traduzir insights complexos em termos claros e relevantes para um público de negócios é igualmente crucial.

<br></br>
## Sobre a entrega do exercício:
-  A solução de seu exercício deve ser entregue em um repositório público do tipo git de sua preferência (github, gitlab, bitbucket ou qualquer outro que preferir). 
-  Espera-se tanto um repositório quanto códigos **bem documentados**: faça seu melhor nesse sentido, adotando as melhores práticas que conhece. 
-  Os resultados precisam ser **reprodutíveis**: 
   -  é fundamental estar contido no repositório de entrega um arquivo **requirements.txt** ou **conda yaml file** com as dependências necessárias para rodar todos os Notebooks.
   -  é fundamental estar contido no repositório de entrega todos os **artefatos** necessários para o consumo do modelo por meio da função de predição (item 3 da seção anterior).
   -   os scripts devem **executar sem erros**.
