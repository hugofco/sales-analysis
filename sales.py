import pandas as pd

list_months = ['june', 'july']


for month in list_months:

    sales_table = pd.read_excel(f'{month}.xlsx')

    if (sales_table['Sales'] > 200).any():
        seller = sales_table.loc[sales_table['Sales']
                                 > 200, 'Seller'].values[0]
        sales = sales_table.loc[sales_table['Sales'] > 200, 'Sales'].values[0]
        print(
            f'In the month of {month}, {seller} reached the goal with a total of {sales} sales.')
