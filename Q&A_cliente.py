
                                        ##############################    RESPOSTAS AUTOMATIZADA DAS RECLAMAÇÕES     ##############################

import openai
import pandas as pd

# Configurar a chave de API do GPT-3
openai.api_key = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

df_sumarizado_com_topico = pd.read_csv('./df_sumarizado_com_topico.csv')
# Função para gerar resposta personalizada com base no sentimento
def gerar_resposta(sentimento, nome, comentario):
    # Adicionar lógica de desconto ou aumento de benefícios com base no sentimento
    if sentimento == 'NEGATIVE':
        prompt_base = f"Cliente: {nome}\nSentimento: {sentimento}\nComentário: {comentario}\nResposta: Oferecemos um desconto de 20% em sua próxima fatura como compensação pela insatisfação. Além disso, incluiremos um pacote de canal infantil como cortesia."
    else:
        prompt_base = f"Cliente: {nome}\nSentimento: {sentimento}\nComentário: {comentario}\nResposta: Agradecemos pelo seu feedback positivo! Como agradecimento, oferecemos um pacote de benefícios exclusivos com um aumento de 20% em seu serviço."

    # Adicionar tópicos específicos ou perguntas relevantes ao prompt
    if 'internet' in comentario.lower():
        prompt_base += "\nTópico: internet"
    elif 'tv' in comentario.lower():
        prompt_base += "\nTópico: tv"
    elif 'fatura' in comentario.lower():
        prompt_base += "\nTópico: fatura"
    

    # Configurar opções para tornar a resposta mais diversificada
    options = {
        "temperature": 0.7,
        "max_tokens": 150,
        "top_p": 0.95
    }

    # Solicitar resposta ao modelo GPT-3
    resposta_personalizada = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=prompt_base,
        **options
    )

    return resposta_personalizada.choices[0].text.strip()

# Aplicar a função para cada linha do DataFrame
for indice, linha in df_sumarizado_com_topico.iterrows():
    nome_cliente = linha['Nome']
    sentimento_cliente = linha['sentimento_descricao']
    comentario_cliente = linha['Comentários']

    # Obter resposta personalizada com base no sentimento
    resposta_personalizada = gerar_resposta(sentimento_cliente, nome_cliente, comentario_cliente)

    # Exibir a resposta personalizada
    print(f"Resposta para {nome_cliente} (Sentimento: {sentimento_cliente}):")
    print(resposta_personalizada)
    print("=" * 50)