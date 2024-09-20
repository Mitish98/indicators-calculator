import streamlit as st

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

st.title("Calculadora de Indicadores")

# Entradas de dados
st.header("Indicadores Padrão")
custo_marketing = st.number_input("Custo Total de Marketing:", min_value=0.0, format="%.2f")
leads_gerados = st.number_input("Número de Leads Gerados:", min_value=0.0, format="%.2f")

if st.button("Calcular CPL"):
    cpl = calcular_cpl(custo_marketing, leads_gerados)
    st.write(f"CPL: R${cpl:.2f}")

receita_obtida = st.number_input("Receita Obtida:", min_value=0.0, format="%.2f")
custo_investimento = st.number_input("Custo Total de Investimento:", min_value=0.0, format="%.2f")

if st.button("Calcular ROI"):
    roi = calcular_roi(receita_obtida, custo_investimento)
    st.write(f"ROI: {roi:.2f}%")

receita_media_cliente = st.number_input("Receita Média por Cliente:", min_value=0.0, format="%.2f")
tempo_retenção = st.number_input("Tempo Médio de Retenção do Cliente:", min_value=0.0, format="%.2f")
margem_lucro = st.number_input("Margem de Lucro:", min_value=0.0, format="%.2f")

if st.button("Calcular LTV"):
    ltv = calcular_ltv(receita_media_cliente, tempo_retenção, margem_lucro)
    st.write(f"LTV: R${ltv:.2f}")

cliques = st.number_input("Número de Cliques:", min_value=0.0, format="%.2f")
impressoes = st.number_input("Número de Impressões:", min_value=0.0, format="%.2f")

if st.button("Calcular CTR"):
    ctr = calcular_ctr(cliques, impressoes)
    st.write(f"CTR: {ctr:.2f}%")

custo_marketing_vendas = st.number_input("Custo Total de Marketing e Vendas:", min_value=0.0, format="%.2f")
novos_clientes = st.number_input("Número de Novos Clientes Adquiridos:", min_value=0.0, format="%.2f")

if st.button("Calcular CAC"):
    cac = calcular_cac(custo_marketing_vendas, novos_clientes)
    st.write(f"CAC: R${cac:.2f}")

pontuacao_promotores = st.number_input("Pontuação de Promotores:", min_value=0.0, format="%.2f")
pontuacao_detratores = st.number_input("Pontuação de Detratores:", min_value=0.0, format="%.2f")

if st.button("Calcular NPS"):
    nps = calcular_nps(pontuacao_promotores, pontuacao_detratores)
    st.write(f"NPS: {nps:.2f}")

clientes_perdidos = st.number_input("Número de Clientes Perdidos:", min_value=0.0, format="%.2f")
clientes_inicial = st.number_input("Número Total de Clientes no Início do Período:", min_value=0.0, format="%.2f")

if st.button("Calcular Churn"):
    churn = calcular_churn(clientes_perdidos, clientes_inicial)
    st.write(f"Churn: {churn:.2f}%")

# Para rodar o Streamlit, use o comando: streamlit run main.py
