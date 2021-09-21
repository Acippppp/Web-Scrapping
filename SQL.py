import mysql.connector
import datetime
import pandas as pd
from urllib.request import urlopen
import time
from bs4 import BeautifulSoup as bs


day = ['23','24','25','26','27','28','29','30']# Pilih Hari Bulan yang Nak Scrape
#01 Harga Borong
#03 Harga Runcit
#04 Harga Ladang
start_time = time.time()
listdf = []
for i in range(0, len(day)):
    try:

        html = urlopen('https://sdvi2.fama.gov.my/price/direct/price/daily_commodityRpt.asp?Pricing=A&LevelCd=04&PricingDt=2021/6/'+ day[i])
        soup = bs(html, 'lxml')
        soup = soup.findAll('tr')[4]
        if 'TIADA MAKLUMAT LAPORAN PADA CARIAN ANDA.' in soup.text:
            print('Data Pada ' + day[i] + ' Hari Bulan Tiada Rekod')
            print(soup)
        else:
            soup = soup.findAll('tr')
            list_runcit = []
            for row in soup:
                each_row = row.findAll('td')
                str_row = str(each_row)
                row_text = bs(str_row,'lxml').get_text()
                list_runcit.append(row_text)
            df = pd.DataFrame(list_runcit)  # Make List to Data Frame
            df = df[0].str.split(',', expand=True)
            date = datetime.date(2021, 6, 23+i)
            date = [date] * len(df)
            df[6] = date
            df = df.values.tolist()
            listdf.extend(df)



    except Exception as e:
        print(e)

df = pd.DataFrame(listdf[0:])
df = df.rename(columns= {0:'Nama_Variety',1:'Gred',2:'Unit',3:'Harga_Tinggi',4:'Harga_Purata',5:'Harga_Rendah',6:'Tarikh'})
df['Nama_Variety'] = df['Nama_Variety'].str.replace('[','')
df['Harga_Rendah'] = df['Harga_Rendah'].str.replace(']','')


#Data Cleaning
x = 'Pusat' # Find x in column first
y = ']' #Find y in column second

#Make list
list_pusat = df['Nama_Variety'].tolist()
list_negeri = df['Gred'].tolist()

#Pusat
for i in range(0, len(list_pusat)):
    if x in list_pusat[i]:
        list_pusat[i] = list_pusat[i]
    else:
        list_pusat[i] = list_pusat[i-1]
#Negeri
for i in range(0, len(list_negeri)):
    if y in list_negeri[i]:
        list_negeri[i] = list_negeri[i]
    else:
        list_negeri[i] = list_negeri[i-1]

df['Pusat'] = list_pusat
df['Negeri'] = list_negeri
df['Pusat'] =df['Pusat'].str.replace('Pusat : ', '')
df['Negeri'] =df['Negeri'].str.replace(']', '')
df = df.dropna()
print(df)
#df.to_csv(r'C:\Users\Hp\Documents\Borong.csv', encoding='utf-8', index=False)


dbhasif = mysql.connector.connect(
    host='*******',
    user='******',
    password='*****',
    port='****',
    database='Database_name'

)
print(dbhasif)

mycursor = dbhasif.cursor()

# creating column list for insertion
cols = "`,`".join([str(i) for i in df.columns.tolist()])


# Insert DataFrame recrds one by one.
for i, row in df.iterrows():
    sql = "INSERT INTO `Harga_Ladang` (`" +cols + "`) VALUES (" + "%s,"*(len(row)-1) + "%s)"
    mycursor.execute(sql, tuple(row))

    # the connection is not autocommitted by default, so we must commit to save our changes
    dbhasif.commit()


