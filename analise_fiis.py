import yfinance as yf
import pandas as pd
from IPython.display import display

# Carregar o arquivo CSV com os tickers dos FIIs
file_path = 'fiis_tickers.csv'  # Substitua pelo nome do arquivo correto
df = pd.read_csv(file_path)

# Verificar se a coluna 'Ticker' está presente
if 'Ticker' in df.columns:
    tickers = df['Ticker'].tolist()  # Listar todos os tickers

    # Inicializar lista para armazenar os resultados
    resultados = []

    for ticker in tickers:
        # Obter os dados do ticker usando yfinance
        try:
            fii = yf.Ticker(ticker)

            # Buscar dados financeiros relevantes
            preco = fii.history(period="1d")['Close'][0]  # Preço atual da cota
            valor_patrimonial_por_acao = fii.info.get('bookValue')  # Valor patrimonial por cota (VP)
            dividend_yield = fii.info.get('dividendYield') * 100  # Dividend Yield (%)
            distrib_dividendos = fii.dividends  # Distribuições de dividendos

            # Calcular P/VP
            p_vp = preco / valor_patrimonial_por_acao if valor_patrimonial_por_acao else None

            # Verificar o histórico de dividendos (último rendimento pago)
            ultimo_dividendo = distrib_dividendos[-1] if not distrib_dividendos.empty else None

            # Adicionar os resultados na lista
            resultados.append({
                'Ticker': ticker,
                'Preço Atual': preco,
                'P/VP': p_vp,
                'Dividend Yield (%)': dividend_yield,
                'Último Dividendo Pago': ultimo_dividendo
            })

        except Exception as e:
            print(f"Erro ao obter dados para {ticker}: {e}")

    # Converter os resultados em um DataFrame
    resultados_df = pd.DataFrame(resultados)

    # Salvar os resultados em um novo arquivo CSV
    resultados_csv_path = 'resultados_fiis.csv'
    resultados_df.to_csv(resultados_csv_path, index=False)

    print("Análise de FIIs concluída. Resultados salvos em 'resultados_fiis.csv'.")

    # Exibir o conteúdo do arquivo CSV em forma de tabela
    try:
        # Carregar o arquivo CSV gerado e exibir a tabela
        resultados_carregados = pd.read_csv(resultados_csv_path)
        print("\nResultados da análise de FIIs:")
        display(resultados_carregados)
    except FileNotFoundError:
        print(f"Erro: O arquivo '{resultados_csv_path}' não foi encontrado.")

else:
    print("Erro: A coluna 'Ticker' não foi encontrada no arquivo CSV.")
