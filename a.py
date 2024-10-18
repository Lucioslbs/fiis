import pandas as pd
import requests
from bs4 import BeautifulSoup

# URL de uma página que lista todos os FIIs
url = "https://www.fundsexplorer.com.br/ranking"

# Fazer a requisição HTTP para buscar os dados
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Localizar os tickers dos FIIs na tabela
table = soup.find('table', {'id': 'table-ranking'})
tickers = []

# Iterar sobre as linhas da tabela e coletar os tickers
for row in table.tbody.find_all('tr'):
    ticker = row.find('td').text.strip()
    tickers.append(ticker)

# Criar um DataFrame com os tickers
df_fiis = pd.DataFrame(tickers, columns=['Ticker'])

# Salvar o DataFrame em um arquivo CSV
df_fiis.to_csv('fiis_tickers.csv', index=False)

print("Arquivo 'fiis_tickers.csv' gerado com sucesso.")
