import pandas as pd
import yfinance as yf



def if_file_empty(filename):
    df = pd.read_csv(filename)
    df = pd.DataFrame(
        columns=['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Dividens',
                 'Stock Splits', 'Code', 'Counter'])
    return df.empty

#https://finance.yahoo.com/quote/5195.KL/history?period1=1296432000&period2=1626048000&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true

def mas_stock_biz_csv():
    mas_df = pd.read_csv('masStockBiz.csv', converters = {'Code': lambda x: str(x)})
    mas_df = mas_df[['Code', 'Stock']]
    mas_list = mas_df.values.tolist()
    return mas_list


def get_timestamp_range(start_date, end_date):
    file_name = 'x_test.csv'
    mas_list = mas_stock_biz_csv()
    num = 1
    data_list = []
    new_list = []
    for i in mas_list:
        for j in range(len(i)):
            if j == 0:
                code = i[j]
                print(code)
            else:
                stock = i[j]
                
        try:
            data = yf.Ticker(f'{code}.KL')
            data = data.history(start=start_date, end=end_date).reset_index()
            data['Code'] = code
            data['Stock'] = stock
            print(data)
            data = data.values.tolist()
            print(data)
            new_list.extend(data)
            num += 1
        except Exception as e:
            continue
    new_df = pd.DataFrame(new_list,
                          columns=['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Dividens',
                                   'Stock Splits', 'Code', 'Counter'])
    new_df.to_csv(file_name, index=False, header=True)
    print(new_df)

#Enter your wanted date period and run it
get_timestamp_range('2021-01-01','2021-07-16')




