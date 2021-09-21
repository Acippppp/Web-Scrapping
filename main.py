import datetime
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

# link that want to Scrap
# 'name' = urlopen('link website')

#########################################################
# Scrape Harga Runcit 29/5/2021
#########################################################

html = urlopen('https://sdvi2.fama.gov.my/price/direct/price/daily_commodityRpt.asp?Pricing=A&LevelCd=03&PricingDt=2021/5/29&PricingDtPrev=2021/5/27')

test = BeautifulSoup(html, 'lxml')
print(test)

# Pilih mana yg nak scrap sahaja
runcit = test.findAll('tr')
print(runcit)


lists_of_runcit = []
for row in runcit:
    each_row = row.findAll('td')
    str_row = str(each_row)
    row_text = BeautifulSoup(str_row, "lxml").get_text()
    lists_of_runcit.append(row_text)
print(lists_of_runcit)



data = pd.DataFrame(lists_of_runcit[1:])
print(data)

# rename column
data = data.rename(columns={0: 'Name'})
print(data)

data = data.drop(labels=[0, 1, 2, 3, 708], axis=0)
print(data)

data = data['Name'].str.split(",", expand = True)
print(data)




#Rename Column
data = data.rename(columns = {0:'Nama_Variety',1:'Gred',2:'Unit',3:'Harga_Tinggi',4:'Harga_Purata',5:'Harga_Rendah'})
print(data)

Tarikh = datetime.date(2021, 0o5, 29)
print(Tarikh)

x=[Tarikh]*len(data)


data['Tarikh'] = x
print(data)
data['Nama_Variety'] = data['Nama_Variety'].str.replace('[','')
data['Harga_Rendah'] = data['Harga_Rendah'].str.replace(']','')


z = data[data['Nama_Variety'].str.contains('Pusat')]
print(z)



pusat = test.findAll('b')
pusat_str = str(pusat)
pusat_text = BeautifulSoup(pusat_str,'lxml').get_text()
print(pusat_text)



joh = ['JOHOR BAHRU,JOHOR']*(47-4)
ked = ['KOTA SETAR,KEDAH']*(90-47)
kel = ['KOTA BHARU,KELANTAN']*(137-90)
mel = ['MELAKA TENGAH,MELAKA']*(182-137)
n9 = ['SEREMBAN,NEGERI SEMBILAN']*(223-182)
pah = ['KUANTAN,PAHANG']*(267-223)
pin = ['SEBERANG PERAI TENGAH,PULAU PINANG']*(308-267)
per = ['KINTA,PERAK']*(346-308)
perl = ['PERLIS,PERLIS']*(389-346)
gsel = ['GOMBAK,SELANGOR']*(432-389)
klasel = ['KLANG,SELANGOR']*(477-432)
petsel = ['PETALING,SELANGOR']*(521-477)
ter = ['KUALA TERENGGANU,TERENGGANU']*(559-521)
sab = ['KOTA KINABALU,SABAH']*(603-559)
sar = ['KUCHING,SARAWAK']*(641-603)
kl = ['KUALA LUMPUR,W.P. KUALA LUMPUR']*(688-641)
labu = ['LABUAN,W.P. LABUAN']*(707-688+1)


joh.extend(ked)
joh.extend(kel)
joh.extend(mel)
joh.extend(n9)
joh.extend(pah)
joh.extend(pin)
joh.extend(per)
joh.extend(perl)
joh.extend(gsel)
joh.extend(klasel)
joh.extend(petsel)
joh.extend(ter)
joh.extend(sab)
joh.extend(sar)
joh.extend(kl)
joh.extend(labu)
print(joh)
print(len(joh))



data['Pusat'] = joh
data = data.dropna()
print(data)
#data.to_csv(r'C:\Users\Hp\Documents\Harga Runcit.csv', encoding='utf-8', index=False)

###############################
# Scrape Harga Runcit 27/5/2021
################################

html1 = urlopen('https://sdvi2.fama.gov.my/price/direct/price/daily_commodityRpt.asp?Pricing=A&LevelCd=03&PricingDt=2021/5/27&PricingDtPrev=2021/5/27')

test1 = BeautifulSoup(html1, 'lxml')
print(test1)

# Pilih mana yg nak scrap sahaja
runcit1 = test1.findAll('tr')
print(runcit1)


lists_of_runcit1 = []
for row in runcit1:
    each_row = row.findAll('td')
    str_row = str(each_row)
    row_text = BeautifulSoup(str_row, "lxml").get_text()
    lists_of_runcit1.append(row_text)
print(lists_of_runcit1)

data1 = pd.DataFrame(lists_of_runcit1[1:])
print(data1)

# rename column
data1 = data1.rename(columns={0: 'Name'})
print(data1)

data1 = data1.drop(labels=[0, 1, 2, 3, 796], axis=0)
print(data1)

data1 = data1['Name'].str.split(",", expand = True)
print(data1)


#Rename Column
data1 = data1.rename(columns = {0:'Nama_Variety',1:'Gred',2:'Unit',3:'Harga_Tinggi',4:'Harga_Purata',5:'Harga_Rendah'})
print(data1)

Tarikh1 = datetime.date(2021, 0o5, 27)
print(Tarikh1)
x1=[Tarikh1]*len(data1)

data1['Tarikh'] = x1
data1['Nama_Variety'] = data1['Nama_Variety'].str.replace('[','')
data1['Harga_Rendah'] = data1['Harga_Rendah'].str.replace(']','')

z1 = data1[data1['Nama_Variety'].str.contains('Pusat')]
print(z1)

joh = ['JOHOR BAHRU,JOHOR']*(45-4)
ked = ['KOTA SETAR,KEDAH']*(88-45)
kel = ['KOTA BHARU,KELANTAN']*(135-88)
mel = ['MELAKA TENGAH,MELAKA']*(180-135)
n9= ['SEREMBAN,NEGERI SEMBILAN']*(221-180)
pah = ['KUANTAN,PAHANG']*(265-221)
pin = ['SEBERANG PERAI TENGAH,PULAU PINANG']*(308-265)
per = ['KINTA,PERAK']*(346-308)
kang = ['KUALA KANGSAR,PERAK']*(362-346)
hulu = ['HULU PERAK,PERAK']*(378-362)
perl = ['PERLIS,PERLIS']*(421-378)
gsel = ['GOMBAK,SELANGOR']*(465-421)
klasel = ['KLANG,SELANGOR']*(510-465)
petsel = ['PETALING,SELANGOR']*(553-510)
ter = ['KUALA TERENGGANU,TERENGGANU']*(592-553)
sab = ['KOTA KINABALU,SABAH']*(636-592)
sar = ['KUCHING,SARAWAK']*(676-636)
sibu = ['SIBU,SARAWAK']*(711-676)
kl = ['KUALA LUMPUR,W.P. KUALA LUMPUR']*(758-711)
labu = ['LABUAN,W.P. LABUAN']*(796-758)

new_list = joh+ked+kel+mel+n9+pah+pin+per+kang+hulu+perl+gsel+klasel+petsel+ter+sab+sar+sibu+kl+labu

data1['Pusat'] = new_list
data1 =data1.dropna()
print(data1)

data = data1.append(data)
print(data)

#save to csv
#data.to_csv(r'C:\Users\Hp\Documents\Harga Runcit.csv', encoding='utf-8', index=False)

####################################
# Scrape Harga Runcit from 25/5/2021
####################################
html2 = urlopen('https://sdvi2.fama.gov.my/price/direct/price/daily_commodityRpt.asp?Pricing=A&LevelCd=03&PricingDt=2021/5/25&PricingDtPrev=2021/5/27')

test2 = BeautifulSoup(html2, 'lxml')
print(test2)

# Pilih mana yg nak scrap sahaja
runcit2 = test2.findAll('tr')
print(runcit2)


lists_of_runcit2 = []
for row in runcit2:
    each_row = row.findAll('td')
    str_row = str(each_row)
    row_text = BeautifulSoup(str_row, "lxml").get_text()
    lists_of_runcit2.append(row_text)
print(lists_of_runcit2)

data2 = pd.DataFrame(lists_of_runcit2[1:])
print(data2)

# rename column
data2 = data2.rename(columns={0: 'Name'})
print(data2)

data2 = data2.drop(labels=[0, 1, 2, 3, 782], axis=0)
print(data2)

data2 = data2['Name'].str.split(",", expand = True)

#Rename Column
data2 = data2.rename(columns = {0:'Nama_Variety',1:'Gred',2:'Unit',3:'Harga_Tinggi',4:'Harga_Purata',5:'Harga_Rendah'})
print(data2)

Tarikh2 = datetime.date(2021, 0o5, 25)
x2=[Tarikh2]*len(data2)

data2['Tarikh'] = x2
data2['Nama_Variety'] = data2['Nama_Variety'].str.replace('[','')
data2['Harga_Rendah'] = data2['Harga_Rendah'].str.replace(']','')

z2 = data2[data2['Nama_Variety'].str.contains('Pusat')]
print(z2)

joh = ['JOHOR BAHRU,JOHOR']*(47-4)
ked = ['KOTA SETAR,KEDAH']*(90-47)
kel = ['KOTA BHARU,KELANTAN']*(140-90)
mel = ['MELAKA TENGAH,MELAKA']*(185-140)
n9= ['SEREMBAN,NEGERI SEMBILAN']*(226-185)
pah = ['KUANTAN,PAHANG']*(270-226)
rompin = ['ROMPIN,PAHANG']*(275-270)
pin = ['SEBERANG PERAI TENGAH,PULAU PINANG']*(320-275)
per = ['KINTA,PERAK']*(358-320)
perl = ['PERLIS,PERLIS']*(404-358)
gsel = ['GOMBAK,SELANGOR']*(447-404)
klasel = ['KLANG,SELANGOR']*(494-447)
petsel = ['PETALING,SELANGOR']*(537-494)
ter = ['KUALA TERENGGANU,TERENGGANU']*(578-537)
sab = ['KOTA KINABALU,SABAH']*(622-578)
sar = ['KUCHING,SARAWAK']*(665-622)
miri = ['MIRI,SARAWAK']*(697-665)
kl = ['KUALA LUMPUR,W.P. KUALA LUMPUR']*(744-697)
labu = ['LABUAN,W.P. LABUAN']*(782-744)

new_list = joh+ked+kel+mel+n9+pah+rompin+pin+per+perl+gsel+klasel+petsel+ter+sab+sar+miri+kl+labu

data2['Pusat'] = new_list
data2 =data2.dropna()
print(data2)

data = data2.append(data)
print(data)

#save to csv
#data.to_csv(r'C:\Users\Hp\Documents\Harga Runcit.csv', encoding='utf-8', index=False)

#########################################################
# Scrape Harga Runcit 22/5/2021
#########################################################

html3 = urlopen('https://sdvi2.fama.gov.my/price/direct/price/daily_commodityRpt.asp?Pricing=A&LevelCd=03&PricingDt=2021/5/22&PricingDtPrev=2021/5/27')

test3 = BeautifulSoup(html3, 'lxml')
print(test3)

# Pilih mana yg nak scrap sahaja
runcit3 = test3.findAll('tr')
print(runcit3)


list_of_runcit3 = []
for row in runcit3:
    each_row = row.findAll('td')
    str_row = str(each_row)
    row_text = BeautifulSoup(str_row, "lxml").get_text()
    list_of_runcit3.append(row_text)
print(list_of_runcit3)



data3 = pd.DataFrame(list_of_runcit3[1:])
print(data3)

# rename column
data3 = data3.rename(columns={0: 'Name'})
print(data3)

data3 = data3.drop(labels=[0, 1, 2, 3, 727], axis=0)

data3 = data3['Name'].str.split(",", expand = True)

#Rename Column
data3 = data3.rename(columns = {0:'Nama_Variety',1:'Gred',2:'Unit',3:'Harga_Tinggi',4:'Harga_Purata',5:'Harga_Rendah'})
print(data3)

Tarikh3 = datetime.date(2021, 0o5, 22)
x3=[Tarikh3]*len(data3)

data3['Tarikh'] = x3
data3['Nama_Variety'] = data3['Nama_Variety'].str.replace('[','')
data3['Harga_Rendah'] = data3['Harga_Rendah'].str.replace(']','')

z3 = data3[data3['Nama_Variety'].str.contains('Pusat')]
print(z3)

joh = ['JOHOR BAHRU,JOHOR']*(47-4)
ked = ['KOTA SETAR,KEDAH']*(90-47)
kel = ['KOTA BHARU,KELANTAN']*(137-90)
mel = ['MELAKA TENGAH,MELAKA']*(182-137)
n9 = ['SEREMBAN,NEGERI SEMBILAN']*(223-182)
pah = ['KUANTAN,PAHANG']*(265-223)
pin = ['SEBERANG PERAI TENGAH,PULAU PINANG']*(308-265)
per = ['KINTA,PERAK']*(345-308)
perl = ['PERLIS,PERLIS']*(388-345)
gsel = ['GOMBAK,SELANGOR']*(431-388)
klasel = ['KLANG,SELANGOR']*(476-431)
petsel = ['PETALING,SELANGOR']*(518-476)
ter = ['KUALA TERENGGANU,TERENGGANU']*(557-518)
sab = ['KOTA KINABALU,SABAH']*(601-557)
sar = ['KUCHING,SARAWAK']*(643-601)
kl = ['KUALA LUMPUR,W.P. KUALA LUMPUR']*(689-643)
labu = ['LABUAN,W.P. LABUAN']*(727-689)

new_list = joh+ked+kel+mel+n9+pah+pin+per+perl+gsel+klasel+petsel+ter+sab+sar+kl+labu

data3['Pusat'] = new_list

data3 = data3.dropna()

data = data3.append(data)
print(data)

#########################################################
# Scrape Harga Runcit 20/5/2021
#########################################################

html4 = urlopen('https://sdvi2.fama.gov.my/price/direct/price/daily_commodityRpt.asp?Pricing=A&LevelCd=03&PricingDt=2021/5/20&PricingDtPrev=2021/5/27')

test4 = BeautifulSoup(html4, 'lxml')
print(test4)

# Pilih mana yg nak scrap sahaja
runcit4 = test4.findAll('tr')
print(runcit4)


list_of_runcit4 = []
for row in runcit4:
    each_row = row.findAll('td')
    str_row = str(each_row)
    row_text = BeautifulSoup(str_row, "lxml").get_text()
    list_of_runcit4.append(row_text)
print(list_of_runcit4)



data4 = pd.DataFrame(list_of_runcit4[1:])
print(data4)

# rename column
data4 = data4.rename(columns={0: 'Name'})
print(data4)

data4 = data4.drop(labels=[0, 1, 2, 3, 762], axis=0)

data4 = data4['Name'].str.split(",", expand = True)

#Rename Column
data4 = data4.rename(columns = {0:'Nama_Variety',1:'Gred',2:'Unit',3:'Harga_Tinggi',4:'Harga_Purata',5:'Harga_Rendah'})
print(data4)

Tarikh4 = datetime.date(2021, 0o5, 20)
x4=[Tarikh4]*len(data4)

data4['Tarikh'] = x4
data4['Nama_Variety'] = data4['Nama_Variety'].str.replace('[','')
data4['Harga_Rendah'] = data4['Harga_Rendah'].str.replace(']','')

z4 = data4[data4['Nama_Variety'].str.contains('Pusat')]
print(z4)

joh = ['JOHOR BAHRU,JOHOR']*(47-4)
ked = ['KOTA SETAR,KEDAH']*(90-47)
kel = ['KOTA BHARU,KELANTAN']*(137-90)
mel = ['MELAKA TENGAH,MELAKA']*(182-137)
n9 = ['SEREMBAN,NEGERI SEMBILAN']*(223-182)
pah = ['KUANTAN,PAHANG']*(268-223)
pin = ['SEBERANG PERAI TENGAH,PULAU PINANG']*(311-268)
per = ['KINTA,PERAK']*(349-311)
perl = ['PERLIS,PERLIS']*(392-349)
gsel = ['GOMBAK,SELANGOR']*(436-392)
klasel = ['KLANG,SELANGOR']*(481-436)
petsel = ['PETALING,SELANGOR']*(523-481)
ter = ['KUALA TERENGGANU,TERENGGANU']*(562-523)
sab = ['KOTA KINABALU,SABAH']*(606-562)
sar = ['KUCHING,SARAWAK']*(645-606)
miri = ['MIRI,SARAWAK']*(677-645)
kl = ['KUALA LUMPUR,W.P. KUALA LUMPUR']*(724-677)
labu = ['LABUAN,W.P. LABUAN']*(762-724)

new_list = joh+ked+kel+mel+n9+pah+pin+per+perl+gsel+klasel+petsel+ter+sab+sar+miri+kl+labu

data4['Pusat'] = new_list

data4 = data4.dropna()

data = data4.append(data)
print(data)
#########################################################
# Scrape Harga Runcit 18/5/2021
#########################################################

html5 = urlopen('https://sdvi2.fama.gov.my/price/direct/price/daily_commodityRpt.asp?Pricing=A&LevelCd=03&PricingDt=2021/5/18&PricingDtPrev=2021/5/27')

test5 = BeautifulSoup(html5, 'lxml')
print(test5)

# Pilih mana yg nak scrap sahaja
runcit5 = test5.findAll('tr')
print(runcit5)


list_of_runcit5 = []
for row in runcit5:
    each_row = row.findAll('td')
    str_row = str(each_row)
    row_text = BeautifulSoup(str_row, "lxml").get_text()
    list_of_runcit5.append(row_text)
print(list_of_runcit5)



data5 = pd.DataFrame(list_of_runcit5[1:])
print(data5)

# rename column
data5 = data5.rename(columns={0: 'Name'})
print(data5)

data5 = data5.drop(labels=[0, 1, 2, 3, 777], axis=0)

data5 = data5['Name'].str.split(",", expand = True)

#Rename Column
data5 = data5.rename(columns = {0:'Nama_Variety',1:'Gred',2:'Unit',3:'Harga_Tinggi',4:'Harga_Purata',5:'Harga_Rendah'})
print(data5)

Tarikh5 = datetime.date(2021, 0o5, 18)
x5=[Tarikh5]*len(data5)

data5['Tarikh'] = x5
data5['Nama_Variety'] = data5['Nama_Variety'].str.replace('[','')
data5['Harga_Rendah'] = data5['Harga_Rendah'].str.replace(']','')

z5 = data5[data5['Nama_Variety'].str.contains('Pusat')]
print(z5)

joh = ['JOHOR BAHRU,JOHOR']*(47-4)
ked = ['KOTA SETAR,KEDAH']*(87-47)
kel = ['KOTA BHARU,KELANTAN']*(137-87)
mel = ['MELAKA TENGAH,MELAKA']*(185-137)
n9 = ['SEREMBAN,NEGERI SEMBILAN']*(226-185)
pah = ['KUANTAN,PAHANG']*(271-226)
rompin = ['ROMPIN,PAHANG'] *(276-271)
pin = ['SEBERANG PERAI TENGAH,PULAU PINANG']*(320-276)
per = ['KINTA,PERAK']*(360-320)
perl = ['PERLIS,PERLIS']*(405-360)
gsel = ['GOMBAK,SELANGOR']*(448-405)
klasel = ['KLANG,SELANGOR']*(495-448)
petsel = ['PETALING,SELANGOR']*(538-495)
ter = ['KUALA TERENGGANU,TERENGGANU']*(576-538)
sab = ['KOTA KINABALU,SABAH']*(620-576)
sar = ['KUCHING,SARAWAK']*(659-620)
miri = ['MIRI,SARAWAK']*(691-659)
kl = ['KUALA LUMPUR,W.P. KUALA LUMPUR']*(739-691)
labu = ['LABUAN,W.P. LABUAN']*(777-739)

new_list = joh+ked+kel+mel+n9+pah+rompin+pin+per+perl+gsel+klasel+petsel+ter+sab+sar+miri+kl+labu

data5['Pusat'] = new_list

data5 = data5.dropna()

data = data5.append(data)
print(data)
data.to_csv(r'C:\Users\Hp\Documents\Harga Runcit.csv', encoding='utf-8', index=False)