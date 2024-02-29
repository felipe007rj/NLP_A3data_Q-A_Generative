# Projeto de Análise de Churn para a A3Data

## Descrição do Projeto

O teste técnico para a vaga de Cientista de Dados da A3Data consiste na exploração de uma base de dados com dados dos clientes e perfil de compra de uma empresa de telecomunicações.

**Objetivo:**
A empresa de telecomunicações contratou a A3Data para avaliar o cenário de churn elevado de seus clientes. Como o produto tem um custo elevado de setup (instalação), a empresa busca uma estratégia para reduzir esse churn. O conhecimento em NLP e LLM é essencial para esta vaga.

**Definição do Problema:**
- Avaliação do churn elevado dos clientes.
- Desenvolvimento de estratégias para redução do churn.

## Entregáveis

Você deverá entregar os seguintes artefatos:

1. **Apresentação dos Resultados (Power Point ou Google Slides):**
   - Apresentação do desafio.
   - Planejamento de entregáveis (inclusive futuros) - Roadmap.
   - Explicação do processo utilizado.
   - Hipóteses levantadas.
   - Análise exploratória.
   - Sumarização das informações textuais.
   - Análise de tópicos relevantes.
   - Parte textual disponível para consulta no modelo de Q&A.
   - Conclusões/insights gerados e sugestão de ações.
   - Estimativa de impacto das ações sugeridas.
   - Fortemente desejável: fine-tuning de modelo open source para a aplicação.

## Análise de Sentimento do Cliente

Adicionamos uma análise de sentimento aos comentários dos clientes. Utilizamos um modelo BERT para classificar os comentários em sentimentos positivos, negativos ou neutros.

# Como Executar

## Instale as Dependências:

Execute o seguinte comando para instalar as bibliotecas necessárias:

pip install -r requirements.txt

# Dependências

- pandas
- transformers
- torch
- matplotlib
- seaborn
- fuzzywuzzy
- openai (para a geração de respostas personalizadas)

## Respostas Personalizadas aos Clientes

Adicionamos uma funcionalidade de resposta personalizada aos clientes com base no sentimento expresso em seus comentários. Utilizamos a API GPT-3 da OpenAI para gerar respostas contextualizadas e relevantes.

# Exemplo de Resposta Personalizada do Código

Aqui está um exemplo de resposta personalizada gerada pelo código `Q&A_cliente.py`:

<sup>Resposta para 1 (Sentimento: NEGATIVE):<br>
Cliente: 1<br>
Sentimento: NEGATIVE<br>
Comentário: "Estou profundamente insatisfeita com o serviço de telefonia fixa. As ligações são constantemente interrompidas, e a qualidade do som é péssima. Além disso, o atendimento ao cliente é ineficiente e não resolve meus problemas. Não recomendo essa empresa de forma alguma."<br>
Resposta: Oferecemos um desconto de 20% em sua próxima fatura como compensação pela insatisfação. Além disso, incluiremos um pacote de canal infantil como cortesia.<br>
Tópico: telefonia</sup><br>
<sub>==================================================</sub>

### Visualização de Dados

![22221](https://github.com/felipe007rj/NLP_A3data_Q-A_Generative/assets/89472224/467d8af5-495e-4b56-9dd9-e4fb069c934d)

