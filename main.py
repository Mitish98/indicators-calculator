import streamlit as st
from collections import Counter
import pandas as pd

# Initialize session state
if 'results' not in st.session_state:
    st.session_state.results = {}

# Function to export results to CSV
def export_results():
    if st.session_state.results:
        df = pd.DataFrame(st.session_state.results.items(), columns=['Indicator', 'Value'])
        return df.to_csv(index=False)
    else:
        return None

# Calculation functions

def calculate_purchase_frequency(total_purchases, clients):
    return total_purchases / clients

def calculate_payback_period(initial_investment, annual_return):
    return initial_investment / annual_return

def calculate_arithmetic_mean(values):
    return sum(values) / len(values)

def calculate_weighted_average(values, weights):
    total_weights = sum(weights)
    return sum(v * w for v, w in zip(values, weights)) / total_weights

def calculate_median(values):
    sorted_values = sorted(values)
    n = len(sorted_values)
    middle = n // 2
    if n % 2 == 0:
        return (sorted_values[middle - 1] + sorted_values[middle]) / 2
    else:
        return sorted_values[middle]

def calculate_mode(values):
    count = Counter(values)
    max_frequency = max(count.values())
    modes = [val for val, freq in count.items() if freq == max_frequency]
    return modes

def calculate_conversion_rate(conversions, total_visits):
    return (conversions / total_visits) * 100

def calculate_growth_rate(current_value, previous_value):
    return ((current_value - previous_value) / previous_value) * 100

def calculate_cpl(marketing_cost, leads_generated):
    return marketing_cost / leads_generated

def calculate_roi(revenue_earned, investment_cost):
    return (revenue_earned - investment_cost) / investment_cost * 100

def calculate_ltv(avg_customer_revenue, retention_time, profit_margin):
    return avg_customer_revenue * retention_time * profit_margin

def calculate_ctr(clicks, impressions):
    return (clicks / impressions) * 100

def calculate_cac(marketing_sales_cost, new_customers):
    return marketing_sales_cost / new_customers

def calculate_nps(promoter_score, detractor_score):
    return promoter_score - detractor_score

def calculate_churn(lost_customers, initial_customers):
    return (lost_customers / initial_customers) * 100

def calculate_average_ticket(total_revenue, number_of_clients):
    return total_revenue / number_of_clients

# Function to add and display results
def add_result(name, value):
    if isinstance(value, list):
        formatted_value = ', '.join(map(str, value))  # Format list as string
    else:
        formatted_value = f"{value:.2f}"  # Format as decimal if not a list
    
    st.session_state.results[name] = value  # Store result in session state
    st.write(f"{name}: {formatted_value}")

# User interface
st.title("Indicators Calculator")
st.write("Page dedicated to calculating indicators for multiple data analysis functionalities.")

# Button to export results
csv_results = export_results()
if csv_results:
    st.download_button("Download CSV File", csv_results, "results.csv", "text/csv")
else:
    st.warning("No results to export.")

# Return on Investment
st.header("Return on Investment", help="Measures investment efficiency, allowing companies to compare projects/campaigns and prioritize those with higher potential returns, justifying marketing and advertising expenses.")
revenue_earned = st.number_input("Revenue Earned:", min_value=0.0, format="%.2f")
investment_cost = st.number_input("Total Cost of Investment:", min_value=0.0, format="%.2f")

if st.button("Calculate ROI"):
    if investment_cost > 0:
        roi = calculate_roi(revenue_earned, investment_cost)
        add_result("ROI", roi)
    else:
        st.warning("The investment cost must be greater than zero.")

# Payback Period
st.header("Payback Period", help="Metric used to find the time it takes for a product/campaign/service to recoup the invested amount. This is crucial for financial sectors to make projections and ensure a safe margin for a particular investment to thrive.")
initial_investment = st.number_input("Initial Investment:", min_value=0.0, format="%.2f")
annual_return = st.number_input("Annual Return:", min_value=0.0, format="%.2f")

if st.button("Calculate Payback Period"):
    if annual_return > 0:
        payback_period = calculate_payback_period(initial_investment, annual_return)
        add_result("Payback Period", payback_period)
    else:
        st.warning("The annual return must be greater than zero.")

# Purchase Frequency
st.header("Purchase Frequency", help="Calculates the number of purchases each customer makes. This metric is ideal for tracking the likelihood of a customer making a cross-sell or up-sell, and essential for monitoring purchase periods.")
total_purchases = st.number_input("Total Number of Purchases:", min_value=0.0, format="%.2f")
clients = st.number_input("Number of Clients:", min_value=0.0, format="%.2f")

if st.button("Calculate Purchase Frequency"):
    if clients > 0:
        purchase_frequency = calculate_purchase_frequency(total_purchases, clients)
        add_result("Purchase Frequency", purchase_frequency)
    else:
        st.warning("The number of clients must be greater than zero.")

# Average Ticket
st.header("Average Ticket", help="The Average Ticket indicator calculates the average amount spent by each customer in their purchases. This indicator is important to understand customer behavior and measure the effectiveness of sales strategies.")
total_revenue = st.number_input("Total Revenue:", min_value=0.0, format="%.2f")
number_of_clients = st.number_input("Number of Clients:", min_value=0)

if st.button("Calculate Average Ticket"):
    if number_of_clients > 0:
        average_ticket = calculate_average_ticket(total_revenue, number_of_clients)
        add_result("Average Ticket", average_ticket)
    else:
        st.warning("The number of clients must be greater than zero.")

# Cost Per Lead
st.header("Cost Per Lead", help="CPL helps measure the effectiveness of marketing campaigns, as campaigns with a low CPL generally indicate good performance. Ideal for allocating budgets efficiently, allowing companies to direct resources to the most profitable campaigns.")
marketing_cost = st.number_input("Total Marketing Cost:", min_value=0.0, format="%.2f")
leads_generated = st.number_input("Number of Leads Generated:", min_value=0.0, format="%.2f")

if st.button("Calculate CPL"):
    if leads_generated > 0:
        cpl = calculate_cpl(marketing_cost, leads_generated)
        add_result("CPL", cpl)
    else:
        st.warning("The number of leads generated must be greater than zero.")

# Customer Acquisition Cost
st.header("Customer Acquisition Cost", help="Represents the total cost involved in acquiring a new customer. Analyzing CAC can reveal areas where acquisition costs are excessive, allowing adjustments in marketing and sales tactics.")
marketing_sales_cost = st.number_input("Total Marketing and Sales Cost:", min_value=0.0, format="%.2f")
new_customers = st.number_input("Number of New Customers Acquired:", min_value=0.0, format="%.2f")

if st.button("Calculate CAC"):
    if new_customers > 0:
        cac = calculate_cac(marketing_sales_cost, new_customers)
        add_result("CAC", cac)
    else:
        st.warning("The number of new customers must be greater than zero.")

# Life Time Value
st.header("Life Time Value", help="Estimates the total value a customer can generate for a company throughout their relationship with the brand, allowing companies to invest more effectively in marketing campaigns to know how much they are willing to spend to acquire a customer. LTV should be compared to the Customer Acquisition Cost (CAC). A significantly higher LTV than CAC indicates a healthy acquisition strategy.")
avg_customer_revenue = st.number_input("Average Revenue per Customer:", min_value=0.0, format="%.2f")
retention_time = st.number_input("Average Customer Retention Time:", min_value=0.0, format="%.2f")
profit_margin = st.number_input("Profit Margin:", min_value=0.0, format="%.2f")

if st.button("Calculate LTV"):
    if retention_time > 0:
        ltv = calculate_ltv(avg_customer_revenue, retention_time, profit_margin)
        add_result("LTV", ltv)
    else:
        st.warning("The average retention time must be greater than zero.")

# Click Through Rate
st.header("Click Through Rate")
clicks = st.number_input("Number of Clicks:", min_value=0.0, format="%.2f")
impressions = st.number_input("Number of Impressions:", min_value=0.0, format="%.2f")

if st.button("Calculate CTR"):
    if impressions > 0:
        ctr = calculate_ctr(clicks, impressions)
        add_result("CTR", ctr)
    else:
        st.warning("The number of impressions must be greater than zero.")

# Net Promoter Score
st.header("Net Promoter Score", help="A metric that measures customer loyalty and their likelihood to recommend a company, product, or service to others.")
promoter_score = st.number_input("Promoter Score:", min_value=0.0, format="%.2f")
detractor_score = st.number_input("Detractor Score:", min_value=0.0, format="%.2f")

if st.button("Calculate NPS"):
    if promoter_score >= 0 and detractor_score >= 0:
        nps = calculate_nps(promoter_score, detractor_score)
        add_result("NPS", nps)
    else:
        st.warning("The promoter and detractor scores must be non-negative.")

# Churn Rate
st.header("Churn Rate", help="Measures the percentage of customers that stop using your product during a certain timeframe. It’s essential for assessing the retention of customers.")
lost_customers = st.number_input("Number of Lost Customers:", min_value=0)
initial_customers = st.number_input("Initial Number of Customers:", min_value=0)

if st.button("Calculate Churn Rate"):
    if initial_customers > 0:
        churn_rate = calculate_churn(lost_customers, initial_customers)
        add_result("Churn Rate", churn_rate)
    else:
        st.warning("The initial number of customers must be greater than zero.")

# Growth Rate
st.header("Growth Rate", help="The Growth Rate is a measure of the increase in size or value of a business over time. Understanding growth is crucial for long-term planning.")
current_value = st.number_input("Current Value:", min_value=0.0, format="%.2f")
previous_value = st.number_input("Previous Value:", min_value=0.0, format="%.2f")

if st.button("Calculate Growth Rate"):
    if previous_value > 0:
        growth_rate = calculate_growth_rate(current_value, previous_value)
        add_result("Growth Rate", growth_rate)
    else:
        st.warning("The previous value must be greater than zero.")


# Inicializa session_state se não existir
if 'results' not in st.session_state:
    st.session_state.results = {}

if 'resultados' not in st.session_state:
    st.session_state.resultados = {}

# Exibe todos os resultados
if st.session_state.results:
    st.subheader("Calculated Results")
    for indicator, value in st.session_state.results.items():
        st.write(f"{indicator}: {value:.2f}" if isinstance(value, (int, float)) else f"{indicator}: {value}")

resultados_keys = list(st.session_state.resultados.keys())
for nome in resultados_keys:
    valor = st.session_state.resultados[nome]
    st.write(f"{nome}: {valor}")
    if st.button(f"Exclude {nome}"):
        del st.session_state.resultados[nome]
        st.success(f"{nome} successfully deleted!")
