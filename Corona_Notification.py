from plyer import notification
import requests
from bs4 import BeautifulSoup
import time

def desk_Notify(title,message):
    notification.notify(
        title=title,
        message=message,
        app_icon=None,
        timeout=5
    )

def getDataURL(url):
    r=requests.get(url)
    return r.text

if __name__=="__main__" :

    usedHtml=getDataURL('https://www.mohfw.gov.in/')
    Extract = BeautifulSoup(usedHtml, 'html.parser')

    MydataStr=""
    for tr in Extract.find_all('tbody')[1].find_all('tr'):
        MydataStr += tr.get_text()
    MydataStr=MydataStr[1:]
    ItemList=MydataStr.split("\n\n")

    states=['Telengana','Odisha','Karnataka']
    for item in ItemList[0:22]:
        dataList=item.split('\n')
        if dataList[1] in states:
            print(dataList)
            final_Title='Covid-19'
            final_Text=f"STATE: {dataList[1]}\n Indian: {dataList[2]} & Foreign: {dataList[3]} \nCured: {dataList[4]} \nDeaths: {dataList[5]}"
            desk_Notify(final_Title,final_Text)

time.sleep(2)