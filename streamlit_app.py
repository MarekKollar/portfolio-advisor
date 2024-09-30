import streamlit as st
import pandas as pd
import math
import yfinance as yf
import matplotlib.pyplot as plt
import plotly.express as px
import openai
import requests
from pathlib import Path
import streamlit as st
from datetime import datetime

# Fetch today's date
today = datetime.today().strftime('%Y-%m-%d')

# Initialize session state to store portfolio
if 'portfolio' not in st.session_state:
    st.session_state['portfolio'] = []

st.sidebar.title("Menu")
option = st.sidebar.selectbox("Select an option", ["Portfolio", "Insights", "Settings"])

if option == "Portfolio":
    st.title("My Portfolio")

    # Display portfolio data if available
    if len(st.session_state['portfolio']) > 0:
        df = pd.DataFrame(st.session_state['portfolio'], columns=['Stock Ticker', 'Quantity', 'Purchase Price'])
        st.write(df)
    else:
        st.write("No stocks in the portfolio yet.")
    
elif option == "Insights":
    st.title("Market Insights")
    # Display AI-generated insight (not implemented)

# Input for adding stocks
ticker = st.text_input("Stock Ticker")
quantity = st.number_input("Quantity", min_value=1)
purchase_price = st.number_input("Purchase Price", min_value=0.0)

if st.button("Add to Portfolio!"):
    # Add stock details to the session state portfolio
    st.session_state['portfolio'].append([ticker, quantity, purchase_price])
    st.success(f"Added {quantity} shares of {ticker} to your portfolio.")

# Fetch stock data
ticker = 'AAPL'
data = yf.download(ticker, interval = "1h", start='2024-01-01', end=today)
df = pd.DataFrame(data)

# Display data in Streamlit
st.title(f'Stock Data for {ticker}')

# Plotly plot
fig_px = px.line(df, x=df.index, y='Close', title='Closing Prices with Plotly')
st.plotly_chart(fig_px)