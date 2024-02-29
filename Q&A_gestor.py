                        
                                        ##############################    GERADOR DE RELATÓRIOS PARA GESTÃO DE RECLAMAÇÕES     ##############################

import openai
import pandas as pd

# Configurar a chave de API do GPT-3
openai.api_key = 'xxxxxxxxxxxxxxxxxxxxxx'

# Carregar o DataFrame df_sumarizado_com_topico do CSV
df_sumarizado_com_topico = pd.read_csv('./df_sumarizado_com_topico.csv')

# Função para gerar um relatório usando o GPT-3
def gerar_relatorio_gpt(prompt_base, df):
    # Adicionar dados específicos do DataFrame ao prompt
    for _, linha in df.iterrows():
        comentario = linha['Comentários']
        sentimento = linha['sentimento_descricao']
        topico = linha['topico']

        # Adicionar informações de cada linha ao prompt
        prompt_base += f"\n\nComentário: {comentario}\nSentimento: {sentimento}\nTópico: {topico}"

    # Configurar opções para tornar a resposta mais diversificada
    options = {
        "temperature": 0.7,
        "max_tokens": 500,
        "top_p": 0.95
    }

    # Solicitar resposta ao modelo GPT-3
    resposta_relatorio = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=prompt_base,
        **options
    )

    return resposta_relatorio['choices'][0]['text'].strip()

# Exemplo de uso
prompt_base = input("Digite o prompt base: ")
relatorio_gpt = gerar_relatorio_gpt(prompt_base, df_sumarizado_com_topico)
print(relatorio_gpt)
