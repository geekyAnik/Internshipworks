from bs4 import BeautifulSoup
import requests
import pandas as pd
a,b,c=[str(z) for z in input('Search the car you in the format BRANDNAME MODELNAME YEAR :') .split() ]
place=input("Enter your place")
pincode=input("Enter your pincode")
url1='https://www.olx.in/{}/q-{}-{}-{}'.format(place,a,b,c)
url2="https://www.cars24.com/buy-used-car?sort=P&search={}%20{}%20{}&storeCityId=8597&pinId={}".format(a,b,c,pincode)
price_list=[]
car_details=[]
kilometer=[]
source=[]
src="Olx.in"

html_text1=requests.get(url1).text
soup=BeautifulSoup(html_text1,'lxml')
cars=soup.find_all('div',class_='IKo3_')
for car in cars:                                                 #olx.in
    price=car.find('span',class_='_89yzn').text
    price_list.append(price)
    details=car.find('span',class_='_2tW1I').text
    car_details.append(details)
    kilo=car.find('span',class_='_2TVI3').text
    kilometer.append(kilo[7:])
    source.append(src)



src2="Cars24.Com"
html_text2=requests.get(url2).text
soups=BeautifulSoup(html_text2,'lxml')
cars_price=soups.find_all('div',class_='_3USiM')
for car24 in cars_price:                                                 #cars24
    cost=car24.find('h3',class_='_6KkG6').text
    price_list.append(cost)
    source.append(src2)

#print(price_list)

kmstravel=soups.find_all('div',class_='_Ecri')
for km in kmstravel:
    kms=km.find("p").span.text
    kilometer.append(kms)

#print(kilometer)

deta=soups.find_all('div',class_='_3ENhq')
for det in deta:
    de=det.find('h5').text
    car_details.append(de)


#print(car_details)
#print(source)
df=pd.DataFrame()


df['Car Details']=car_details
df['Price']=price_list
df['Kilometer Traveled']=kilometer
df['Source']=source
df.index+=1

df.to_excel('UsedCar.xlsx',index=True)