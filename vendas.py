import pandas as pd

lista_meses = ['junho', 'julho']



for mes in lista_meses: 
    
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    
    if (tabela_vendas['Vendas'] > 200).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 200, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 200, 'Vendas'].values[0]
        print(f'No mês {mes} o funcionário {vendedor} atingiu a meta com um total de {vendas} vendas')


