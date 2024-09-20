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
        df.to_csv('resultados.csv', index=False)
        st.success("Resultados exportados com sucesso!")
    else:
        st.warning("Nenhum resultado para exportar.")

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
if st.button("Exportar Resultados"):
    exportar_resultados()

# Custo por Lead
st.header("Custo por Lead")
custo_marketing = st.number_input("Custo Total de Marketing:", min_value=0.0, format="%.2f")
leads_gerados = st.number_input("Número de Leads Gerados:", min_value=0.0, format="%.2f")

if st.button("Calcular CPL"):
    if leads_gerados > 0:
        cpl = calcular_cpl(custo_marketing, leads_gerados)
        adicionar_resultado("CPL", cpl)
    else:
        st.warning("O número de leads gerados deve ser maior que zero.")

# Return on Investment
st.header("Return on Investment")
receita_obtida = st.number_input("Receita Obtida:", min_value=0.0, format="%.2f")
custo_investimento = st.number_input("Custo Total de Investimento:", min_value=0.0, format="%.2f")

if st.button("Calcular ROI"):
    if custo_investimento > 0:
        roi = calcular_roi(receita_obtida, custo_investimento)
        adicionar_resultado("ROI", roi)
    else:
        st.warning("O custo de investimento deve ser maior que zero.")

# Life Time Value
st.header("Life Time Value")
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

# Custo de Aquisição de Clientes
st.header("Custo de Aquisição de Clientes")
custo_marketing_vendas = st.number_input("Custo Total de Marketing e Vendas:", min_value=0.0, format="%.2f")
novos_clientes = st.number_input("Número de Novos Clientes Adquiridos:", min_value=0.0, format="%.2f")

if st.button("Calcular CAC"):
    if novos_clientes > 0:
        cac = calcular_cac(custo_marketing_vendas, novos_clientes)
        adicionar_resultado("CAC", cac)
    else:
        st.warning("O número de novos clientes deve ser maior que zero.")

# Net Promoter Score
st.header("Net Promoter Score")
pontuacao_promotores = st.number_input("Pontuação de Promotores:", min_value=0.0, format="%.2f")
pontuacao_detratores = st.number_input("Pontuação de Detratores:", min_value=0.0, format="%.2f")

if st.button("Calcular NPS"):
    nps = calcular_nps(pontuacao_promotores, pontuacao_detratores)
    adicionar_resultado("NPS", nps)

# Churn
st.header("Churn")
clientes_perdidos = st.number_input("Número de Clientes Perdidos:", min_value=0.0, format="%.2f")
clientes_inicial = st.number_input("Número Total de Clientes no Início do Período:", min_value=0.0, format="%.2f")

if st.button("Calcular Churn"):
    if clientes_inicial > 0:
        churn = calcular_churn(clientes_perdidos, clientes_inicial)
        adicionar_resultado("Churn", churn)
    else:
        st.warning("O número total de clientes no início do período deve ser maior que zero.")

# Média Aritmética
st.header("Média Aritmética")
valores_aritmetica = st.text_input("Insira os valores separados por vírgula:", "1,2,3,4,5", key="media_aritmetica")
if st.button("Calcular Média Aritmética"):
    valores = list(map(float, valores_aritmetica.split(',')))
    media_aritmetica = calcular_media_aritmetica(valores)
    adicionar_resultado("Média Aritmética", media_aritmetica)

# Média Ponderada
st.header("Média Ponderada")
valores_ponderada = st.text_input("Insira os valores separados por vírgula:", "1,2,3", key="media_ponderada")
pesos_ponderada = st.text_input("Insira os pesos separados por vírgula:", "0.1,0.2,0.7", key="pesos_ponderada")
if st.button("Calcular Média Ponderada"):
    valores = list(map(float, valores_ponderada.split(',')))
    pesos = list(map(float, pesos_ponderada.split(',')))
    media_ponderada = calcular_media_ponderada(valores, pesos)
    adicionar_resultado("Média Ponderada", media_ponderada)

# Mediana
st.header("Mediana")
valores_mediana = st.text_input("Insira os valores separados por vírgula:", "1,2,3,4,5", key="mediana")
if st.button("Calcular Mediana"):
    valores = list(map(float, valores_mediana.split(',')))
    mediana = calcular_mediana(valores)
    adicionar_resultado("Mediana", mediana)

# Moda
st.header("Moda")
valores_moda = st.text_input("Insira os valores separados por vírgula:", "1,2,2,3,4", key="moda")
if st.button("Calcular Moda"):
    valores = list(map(float, valores_moda.split(',')))
    moda = calcular_moda(valores)
    adicionar_resultado("Moda", moda)

# Exibir resultados atuais
st.subheader("Resultados Calculados")
resultados_keys = list(st.session_state.resultados.keys())  # Cópia das chaves
for nome in resultados_keys:
    valor = st.session_state.resultados[nome]
    st.write(f"{nome}: {valor}")
    if st.button(f"Excluir {nome}"):
        del st.session_state.resultados[nome]
        st.success(f"{nome} excluído com sucesso!")
