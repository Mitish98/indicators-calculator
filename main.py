import streamlit as st
from collections import Counter
import pandas as pd

# Inicializa o estado da sessão
if 'resultados' not in st.session_state:
    st.session_state.resultados = {}

# Função para exportar resultados para CSV
def exportar_resultados():
    if st.session_state.resultados:
        df = pd.DataFrame(st.session_state.resultados.items(), columns=['Indicador', 'Valor'])
        return df.to_csv(index=False)
    else:
        return None

# Funções para cálculos
def calcular_media_aritmetica(valores):
    return sum(valores) / len(valores)

def calcular_media_ponderada(valores, pesos):
    total_pesos = sum(pesos)
    return sum(v * p for v, p in zip(valores, pesos)) / total_pesos

def calcular_mediana(valores):
    valores_ordenados = sorted(valores)
    n = len(valores_ordenados)
    meio = n // 2
    if n % 2 == 0:
        return (valores_ordenados[meio - 1] + valores_ordenados[meio]) / 2
    else:
        return valores_ordenados[meio]

def calcular_moda(valores):
    contagem = Counter(valores)
    frequencia_maxima = max(contagem.values())
    modas = [valor for valor, frequencia in contagem.items() if frequencia == frequencia_maxima]
    return modas

def calcular_taxa_conversao(conversoes, total_visitas):
    return (conversoes / total_visitas) * 100

def calcular_taxa_crescimento(valor_atual, valor_anterior):
    return ((valor_atual - valor_anterior) / valor_anterior) * 100

def calcular_cpl(custo_marketing, leads_gerados):
    return custo_marketing / leads_gerados

def calcular_roi(receita_obtida, custo_investimento):
    return (receita_obtida - custo_investimento) / custo_investimento * 100

def calcular_ltv(receita_media_cliente, tempo_retenção, margem_lucro):
    return receita_media_cliente * tempo_retenção * margem_lucro

def calcular_ctr(cliques, impressoes):
    return (cliques / impressoes) * 100

def calcular_cac(custo_marketing_vendas, novos_clientes):
    return custo_marketing_vendas / novos_clientes

def calcular_nps(pontuacao_promotores, pontuacao_detratores):
    return pontuacao_promotores - pontuacao_detratores

def calcular_churn(clientes_perdidos, clientes_inicial):
    return (clientes_perdidos / clientes_inicial) * 100

# Função para adicionar e exibir resultados
def adicionar_resultado(nome, valor):
    if isinstance(valor, list):
        valor_formatado = ', '.join(map(str, valor))  # Formata a lista como string
    else:
        valor_formatado = f"{valor:.2f}"  # Formata como decimal se não for lista
    
    st.session_state.resultados[nome] = valor  # Armazena o resultado no estado da sessão
    st.write(f"{nome}: {valor_formatado}")

# Interface do usuário
st.title("Calculadora de Indicadores")
st.write("Página voltada para o cálculo de indicadores para múltiplas funcionalidades de análise de dados.")

# Botão para exportar resultados
csv_resultados = exportar_resultados()
if csv_resultados:
    st.download_button("Baixar Resultados como CSV", csv_resultados, "resultados.csv", "text/csv")
else:
    st.warning("Nenhum resultado para exportar.")

# Return on Investment
st.header("Return on Investment", help="Avalia a eficiência de um investimento, ajudando empresas a entenderem o retorno que estão obtendo em relação ao que foi investido. Facilita a comparação entre diferentes projetos ou campanhas, permitindo priorizar aqueles com maior retorno potencial para justificar despesas em marketing, publicidade ou qualquer outra área para mostrar o valor gerado por esses investimentos.")
receita_obtida = st.number_input("Receita Obtida:", min_value=0.0, format="%.2f")
custo_investimento = st.number_input("Custo Total de Investimento:", min_value=0.0, format="%.2f")

if st.button("Calcular ROI"):
    if custo_investimento > 0:
        roi = calcular_roi(receita_obtida, custo_investimento)
        adicionar_resultado("ROI", roi)
    else:
        st.warning("O custo de investimento deve ser maior que zero.")

# Custo por Lead
st.header("Custo por Lead", help="O CPL ajuda a medir a eficácia das campanhas de marketing, já que campanhas com um CPL baixo geralmente indicam uma boa performance. Ideal para ajudar a alocar orçamentos de forma eficiente, permitindo que as empresas direcionem recursos para as campanhas mais rentáveis ao testar diferentes canais para identificar quais geram leads a um menor custo")
custo_marketing = st.number_input("Custo Total de Marketing:", min_value=0.0, format="%.2f")
leads_gerados = st.number_input("Número de Leads Gerados:", min_value=0.0, format="%.2f")

if st.button("Calcular CPL"):
    if leads_gerados > 0:
        cpl = calcular_cpl(custo_marketing, leads_gerados)
        adicionar_resultado("CPL", cpl)
    else:
        st.warning("O número de leads gerados deve ser maior que zero.")

# Custo de Aquisição de Clientes
st.header("Custo de Aquisição de Clientes", help="Representa o custo total envolvido na aquisição de um novo cliente. Analisar o CAC pode revelar áreas onde os custos de aquisição são excessivos, permitindo ajustes nas táticas de marketing e vendas.  ")
custo_marketing_vendas = st.number_input("Custo Total de Marketing e Vendas:", min_value=0.0, format="%.2f")
novos_clientes = st.number_input("Número de Novos Clientes Adquiridos:", min_value=0.0, format="%.2f")

if st.button("Calcular CAC"):
    if novos_clientes > 0:
        cac = calcular_cac(custo_marketing_vendas, novos_clientes)
        adicionar_resultado("CAC", cac)
    else:
        st.warning("O número de novos clientes deve ser maior que zero.")

# Life Time Value
st.header("Life Time Value", help="Estima o valor total que um cliente pode gerar para uma empresa durante toda a sua relação com a marca, permitindo que as empresas invistam de forma mais eficaz em campanhas de marketing para saber quanto estão dispostas a gastar para adquirir um cliente. O LTV deve ser comparado ao Custo de Aquisição de Clientes (CAC). Um LTV significativamente maior que o CAC indica uma estratégia de aquisição saudável.")
receita_media_cliente = st.number_input("Receita Média por Cliente:", min_value=0.0, format="%.2f")
tempo_retenção = st.number_input("Tempo Médio de Retenção do Cliente:", min_value=0.0, format="%.2f")
margem_lucro = st.number_input("Margem de Lucro:", min_value=0.0, format="%.2f")

if st.button("Calcular LTV"):
    if tempo_retenção > 0:
        ltv = calcular_ltv(receita_media_cliente, tempo_retenção, margem_lucro)
        adicionar_resultado("LTV", ltv)
    else:
        st.warning("O tempo médio de retenção deve ser maior que zero.")

# Click Through Rate
st.header("Click Through Rate")
cliques = st.number_input("Número de Cliques:", min_value=0.0, format="%.2f")
impressoes = st.number_input("Número de Impressões:", min_value=0.0, format="%.2f")

if st.button("Calcular CTR"):
    if impressoes > 0:
        ctr = calcular_ctr(cliques, impressoes)
        adicionar_resultado("CTR", ctr)
    else:
        st.warning("O número de impressões deve ser maior que zero.")

# Net Promoter Score
st.header("Net Promoter Score", help="Métrica que mede a lealdade dos clientes e a probabilidade de eles recomendarem uma empresa, produto ou serviço a outros. O NPS é obtido a partir de uma única pergunta enviada aos clientes 'Em uma escala de 0 a 10, qual a probabilidade de você recomendar nossa empresa a um amigo ou colega?' Com base nas respostas, os clientes são classificados em três categorias: Promotores (nota 9-10): Clientes fiéis que recomendam a empresa. / Neutros (nota 7-8): Clientes satisfeitos, mas não necessariamente leais. / Detratores (nota 0-6): Clientes insatisfeitos que podem prejudicar a reputação da empresa. Além da pontuação numérica, coletar feedback qualitativo pode oferecer contexto e profundidade às respostas, ajudando a entender as razões por trás das classificações.")
pontuacao_promotores = st.number_input("Pontuação de Promotores:", min_value=0.0, format="%.2f")
pontuacao_detratores = st.number_input("Pontuação de Detratores:", min_value=0.0, format="%.2f")

if st.button("Calcular NPS"):
    nps = calcular_nps(pontuacao_promotores, pontuacao_detratores)
    adicionar_resultado("NPS", nps)

# Churn
st.header("Churn", help="Métrica que indica a porcentagem de clientes que interrompem o uso de um serviço ou produto em um determinado período. Ao entender as causas do churn, as empresas podem desenvolver estratégias específicas para melhorar a retenção e minimizar a perda de clientes.")
clientes_perdidos = st.number_input("Número de Clientes Perdidos:", min_value=0.0, format="%.2f")
clientes_inicial = st.number_input("Número Total de Clientes no Início do Período:", min_value=0.0, format="%.2f")

if st.button("Calcular Churn"):
    if clientes_inicial > 0:
        churn = calcular_churn(clientes_perdidos, clientes_inicial)
        adicionar_resultado("Churn", churn)
    else:
        st.warning("O número total de clientes no início do período deve ser maior que zero.")

# Média Aritmética
st.header("Média Aritmética", help="Medida central comum usada para entender a tendência de dados, valores extremos podem distorcer a média, o que exige cuidado ao interpretar.")
valores_aritmetica = st.text_input("Insira os valores separados por vírgula:", "1,2,3,4,5", key="media_aritmetica")
if st.button("Calcular Média Aritmética"):
    valores = list(map(float, valores_aritmetica.split(',')))
    media_aritmetica = calcular_media_aritmetica(valores)
    adicionar_resultado("Média Aritmética", media_aritmetica)

# Média Ponderada
st.header("Média Ponderada", help="A média ponderada leva em consideração a importância de cada valor no conjunto, atribuindo pesos a eles. A média ponderada oferece uma visão mais precisa quando diferentes valores têm diferentes importâncias.")
valores_ponderada = st.text_input("Insira os valores separados por vírgula:", "1,2,3", key="media_ponderada")
pesos_ponderada = st.text_input("Insira os pesos separados por vírgula:", "0.1,0.2,0.7", key="pesos_ponderada")
if st.button("Calcular Média Ponderada"):
    valores = list(map(float, valores_ponderada.split(',')))
    pesos = list(map(float, pesos_ponderada.split(',')))
    media_ponderada = calcular_media_ponderada(valores, pesos)
    adicionar_resultado("Média Ponderada", media_ponderada)

# Mediana
st.header("Mediana", help="A mediana é o valor central de um conjunto de dados ordenados. Se houver um número ímpar de valores, a mediana é o valor central; se houver um número par, é a média dos dois valores centrais. A mediana é menos afetada por valores extremos, oferecendo uma medida mais robusta em distribuições assimétricas, ideal para descrever distribuições enviesadas.")
valores_mediana = st.text_input("Insira os valores separados por vírgula:", "1,2,3,4,5", key="mediana")
if st.button("Calcular Mediana"):
    valores = list(map(float, valores_mediana.split(',')))
    mediana = calcular_mediana(valores)
    adicionar_resultado("Mediana", mediana)

# Moda
st.header("Moda", help="A moda é o valor que mais aparece em um conjunto de dados. Ao contrário da média e da mediana, a moda não leva em conta o valor exato, mas sim a frequência. Utilizada para entender qual é a escolha mais comum, como o produto mais vendido. Um conjunto de dados pode ter mais de uma moda (bimodal ou multimodal).")
valores_moda = st.text_input("Insira os valores separados por vírgula:", "1,2,2,3,4", key="moda")
if st.button("Calcular Moda"):
    valores = list(map(float, valores_moda.split(',')))
    modas = calcular_moda(valores)
    adicionar_resultado("Moda", modas)

st.header("Taxa de Conversão" , help="Mede o percentual de pessoas que realizaram uma ação desejada (como uma compra) em relação ao número total de pessoas que interagiram com uma campanha ou site.")
conversoes = st.number_input("Número de Conversões:", min_value=0.0, format="%.2f", key="conversoes")
total_visitas = st.number_input("Número Total de Visitas:", min_value=0.0, format="%.2f", key="total_visitas")

if st.button("Calcular Taxa de Conversão"):
    if total_visitas > 0:
        taxa_conversao = calcular_taxa_conversao(conversoes, total_visitas)
        adicionar_resultado("Taxa de Conversão", taxa_conversao)
    else:
        st.warning("O número total de visitas deve ser maior que zero.")

# Taxa de Crescimento
st.header("Taxa de Crescimento", help="A taxa de crescimento mede o aumento percentual de uma variável (como receita, número de clientes, etc.) em relação a um período anterior.")
valor_atual = st.number_input("Valor Atual:", min_value=0.0, format="%.2f", key="valor_atual")
valor_anterior = st.number_input("Valor Anterior:", min_value=0.0, format="%.2f", key="valor_anterior")

if st.button("Calcular Taxa de Crescimento"):
    if valor_anterior > 0:
        taxa_crescimento = calcular_taxa_crescimento(valor_atual, valor_anterior)
        adicionar_resultado("Taxa de Crescimento", taxa_crescimento)
    else:
        st.warning("O valor anterior deve ser maior que zero.")

# Exibir resultados atuais
st.subheader("Resultados Calculados")
resultados_keys = list(st.session_state.resultados.keys())  # Cópia das chaves
for nome in resultados_keys:
    valor = st.session_state.resultados[nome]
    st.write(f"{nome}: {valor}")
    if st.button(f"Excluir {nome}"):
        del st.session_state.resultados[nome]
        st.success(f"{nome} excluído com sucesso!")
