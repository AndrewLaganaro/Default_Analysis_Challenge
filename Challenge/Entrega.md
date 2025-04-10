<br></br>
## Sobre a entrega do exercício:
-  A solução de seu exercício deve ser entregue em um repositório público do tipo git de sua preferência (github, gitlab, bitbucket ou qualquer outro que preferir). 
-  Espera-se tanto um repositório quanto códigos **bem documentados**: faça seu melhor nesse sentido, adotando as melhores práticas que conhece. 
-  Os resultados precisam ser **reprodutíveis**: 
   -  é fundamental estar contido no repositório de entrega um arquivo **requirements.txt** ou **conda yaml file** com as dependências necessárias para rodar todos os Notebooks.
   -  é fundamental estar contido no repositório de entrega todos os **artefatos** necessários para o consumo do modelo por meio da função de predição (item 3 da seção anterior).
   -   os scripts devem **executar sem erros**.


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

