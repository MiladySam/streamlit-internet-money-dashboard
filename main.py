import yfinance as yf
import streamlit as st


from PIL import Image
from urllib.request import urlopen

st.title("Daily Price")
st.header("Dashboard")


# Définit les cryptomonnaies à suivre
Bitcoin = "BTC-USD"
Ethereum = "ETH-USD"
pepecoin = "PEPE24478-USD"
bittensor = "TAO22974-USD"
dogecoin = "DOGE-USD"  


# Utilise l'API yfinance pour récupérer les données de prix
BTC_data = yf.Ticker(Bitcoin)
ETH_data = yf.Ticker(Ethereum)
PEPE_data = yf.Ticker(pepecoin)
TAO_data = yf.Ticker(bittensor)
DOGE_data = yf.Ticker(dogecoin)




# Récupère l'historique des prix pour chaque cryptomonnaie
BTC_hist = BTC_data.history(period="max")
ETH_hist = ETH_data.history(period="max")
PEPE_hist = PEPE_data.history(period="max")
TAO_hist = TAO_data.history(period="max")
DOGE_hist = DOGE_data.history(period="max")



# Récupère les données de prix pour chaque cryptomonnaie pour la date du 01 avril 2024
BTC = yf.download(Bitcoin, start="2024-04-01", end="2024-04-01")
ETH = yf.download(Ethereum, start="2024-04-01", end="2024-04-01")
DOGE = yf.download(dogecoin, start="2024-04-01", end="2024-04-01")
PEPE = yf.download(pepecoin, start="2024-04-01", end="2024-04-01")
TAO = yf.download(bittensor, start="2024-04-01", end="2024-04-01")


# Affiche les données de prix
st.write("Bitcoin")
imgBtc = Image.open(urlopen('https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Bitcoin.svg/1200px-Bitcoin.svg.png'))
st.image(imgBtc, width=25)

