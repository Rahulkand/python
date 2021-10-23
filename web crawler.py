import pandas
import requests
from bs4 import BeautifulSoup
from pandas import DataFrame
tv_info=[]
url="https://www.amazon.in/s?k=tv+43+%2B+inch+smart+tv&ref=nb_sb_ss_ts-doa-p_5_2"
head={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"}
response=requests.get(url=url,headers=head)
content=response.content
read=BeautifulSoup(content,"html.parser")
all_tv=read.find_all("div", {"data-component-type":"s-impression-logger"})
for tv in range (0,len(all_tv),1):
    tv_dict={}
    tv_dict["name"]=all_tv[tv].find("span",{"class":"a-size-medium a-color-base a-text-normal"}).text
    tv_dict["price"]=all_tv[tv].find("span", {"class":"a-price-whole"}).text
    tv_dict["rating"]=all_tv[tv].find("div" ,{"class":"a-row a-size-small"}).text
    tv_info.append(tv_dict)

data=pandas.DataFrame(tv_info)
data.to_csv("tv_info.csv")


