import yfinance as yf
import streamlit as st

from PIL import Image
from urllib.request import urlopen

st.title("Daily Price")
st.header("Dashboard")

# Utilise l'API yfinance pour récupérer les données de prix

Bitcoin = yf.Ticker("BTC-USD")
Ethereum = yf.Ticker("ETH-USD")
pepecoin = yf.Ticker("PEPE-USD")
bittensor = yf.Ticker("TAO-USD")  
dogecoin = yf.Ticker("DOGE-USD")   

# Récupère l'historique des prix pour chaque cryptomonnaie
Bitcoin_data = Bitcoin.history(period="1d")
Ethereum_data = Ethereum.history(period="1d")
pepe_data = pepecoin.history(period="1d")
tao_data = bittensor.history(period="1d")
doge_data = dogecoin.history(period="1d")


BTC = yf.download(Bitcoin, start="2024-04-01", end="2024-04-01")
ETH = yf.download(Ethereum, start="2024-04-01", end="2024-04-01")
DOGE = yf.download(dogecoin, start="2024-04-01", end="2024-04-01")
PEPE = yf.download(pepecoin, start="2024-04-01", end="2024-04-01")
TAO = yf.download(bittensor, start="2024-04-01", end="2024-04-01")