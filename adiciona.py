import pandas as pd

# Caminho do arquivo CSV contendo os tickers de FIIs
file_path = '/mnt/data/fiis_tickers.csv'

# Carregar o arquivo CSV
df = pd.read_csv(file_path)

# Adicionar '.SA' a todos os tickers
df['Ticker'] = df['Ticker'] + '.SA'

# Salvar o arquivo CSV modificado no diretório atual
df.to_csv('fiis_tickers_modificados.csv', index=False)

print("Arquivo 'fiis_tickers_modificados.csv' gerado com sucesso no diretório atual.")
