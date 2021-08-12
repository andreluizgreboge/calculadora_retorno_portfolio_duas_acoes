import yfinance as yf

STOCK_A = input('Escreva o ticker da primeira ação (exemplo GOOG, ticker US Stock ou ITUB4.SA, ticker Ação Brasileira): ')
STOCK_B = input('Escreva o ticker da segunda ação (exemplo GOOG, ticker US Stock ou ITUB4.SA, ticker Ação Brasileira): ')

dia_inicio = input('Escreva o dia de início: ')
mes_inicio = input('Escreva o mês de início: ')
ano_inicio = input('Escreva o ano início: ')
data_inicio = ano_inicio+'-'+mes_inicio+'-'+dia_inicio
print("data inical "+ data_inicio)

dia_fim = input('Escreva o dia de início: ')
mes_fim = input('Escreva o mes de início: ')
ano_fim = input('Escreva o ano de início: ')
data_fim = ano_fim+'-'+mes_fim+'-'+dia_fim
print("data final "+ data_fim)

acao1 = yf.download([STOCK_A], start=data_inicio,end=data_fim)
acao1_close = acao1['Adj Close'].pct_change()

acao2 = yf.download([STOCK_B], start=data_inicio,end=data_fim)
acao2_close = acao2['Adj Close'].pct_change()

weight = [0.20,0.40,0.60,0.80]

for wa in weight:
    wa
    wb = 1 - wa
    portfolio = wa * acao1_close.mean() + wb * acao2_close.mean()
    prct_return = portfolio * 100
    prct_return = str(round(prct_return, 3))
    print(str(round(wa * 100, 2)), f'% de alocação em {STOCK_A} e', str(round(wb * 100, 2)),
          f'% de alocação em {STOCK_B} gerou Portfolio Return de:', prct_return, "%")


