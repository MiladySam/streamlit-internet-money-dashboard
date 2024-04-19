import yfinance as yf
import streamlit as st
import datetime

from PIL import Image
from urllib.request import urlopen

st.title("Daily Price  Dashboard")



# Définit les cryptomonnaies à suivre
Bitcoin = "BTC-USD"
Ethereum = "ETH-USD"
pepecoin = "PEPECOIN-USD"
dogecoin = "DOGE-USD"
celestia = "TIA22861-USD"  


# Utilise l'API yfinance pour récupérer les données de prix
BTC_data = yf.Ticker(Bitcoin)
ETH_data = yf.Ticker(Ethereum)
PEPE_data = yf.Ticker(pepecoin)
DOGE_data = yf.Ticker(dogecoin)
CELESTIA_data = yf.Ticker(celestia)




# Récupère l'historique des prix pour chaque cryptomonnaie
BTC_hist = BTC_data.history(period="max")
ETH_hist = ETH_data.history(period="max")
PEPE_hist = PEPE_data.history(period="max")

DOGE_hist = DOGE_data.history(period="max")
TIA_hist = CELESTIA_data.history(period="max")





# Récupère les données de prix pour chaque cryptomonnaie pour chaque jour

# Obtient la date d'hier et aujourd'hui
today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)

# Télécharge les données de prix
BTC = yf.download(Bitcoin, start=yesterday, end=today)
ETH = yf.download(Ethereum, start=yesterday, end=today)
DOGE = yf.download(dogecoin,start=yesterday, end=today)
PEPE = yf.download(pepecoin,start=yesterday, end=today)
TIA = yf.download(celestia,start=yesterday, end=today)


# Affiche les données de prix
st.header("Bitcoin")
imgBtc = Image.open(urlopen('https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Bitcoin.svg/1200px-Bitcoin.svg.png'))
st.image(imgBtc, width=35)

#affiche du tableau des prix
st.table(BTC)

st.line_chart(BTC_hist.Close)


# Ethereum
st.header("Ethereum")
imgEth = Image.open(urlopen(' https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Ethereum_logo_2014.svg/1200px-Ethereum_logo_2014.svg.png'))
st.image(imgEth, width=25)
st.table(ETH)
st.line_chart(ETH_hist.Close)

# Pepecoin

st.header("Pepecoin")
imgPepe = Image.open('images/pepe.png')
st.image(imgPepe, width=45)
st.table(PEPE)
st.line_chart(PEPE_hist.Close)




# Dogecoin
st.header("Dogecoin")
imgDoge = Image.open('images/Dogecoin_Logo.png')
st.image(imgDoge, width=35)
st.table(DOGE)
st.line_chart(DOGE_hist.Close)


# Celestia
st.header("Celestia")
imgTia = Image.open('images/tia.png')
st.image(imgTia, width=35)
st.table(TIA)
st.line_chart(TIA_hist.Close)