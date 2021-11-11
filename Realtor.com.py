import requests
from bs4 import BeautifulSoup
import pandas as pd
from tkinter import *
import time
from tkinter.messagebox import showinfo


def start():
    headers = {
        'authority': 'www.realtor.com',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Mobile Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://www.realtor.com/',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': 'split=n; split_tcv=160; __vst=e6f0cb42-51f8-470c-85ba-492ba9e26d35; __ssn=d4358bf0-c9dc-4ba3-868f-12aa91cb118c; __ssnstarttime=1636570706; __split=70; AMCVS_8853394255142B6A0A4C98A4%40AdobeOrg=1; G_ENABLED_IDPS=google; srchID=fb7374ebe8e24cbaa70b20cda9373426; criteria=pg%3D1%26sprefix%3D%252Frealestateandhomes-search%26area_type%3Dpostal_code%26search_type%3Dpostal_code%26city%3DRichmond%26postal_code%3D77469%26zip%3D77469%26state_code%3DTX%26state_id%3DTX%26lat%3D29.492986%26long%3D-95.706919%26county_fips%3D48157%26county_fips_multi%3D48157%26loc%3D77469%252C%2520Richmond%252C%2520TX%26locSlug%3D77469; user_activity=return; last_ran=-1; last_ran_threshold=1636570732648; AMCV_8853394255142B6A0A4C98A4%40AdobeOrg=-1124106680%7CMCIDTS%7C18942%7CMCMID%7C75564293837333409987083810661096784126%7CMCAID%7CNONE%7CMCOPTOUT-1636577933s%7CNONE%7CvVersion%7C5.2.0; g_state={"i_p":1636577938658,"i_l":1}',
        'if-none-match': '"eab64-qYulCq7WkZXcmAsVAVZ7nmQzAdk"',
    }
    zip=int(e1.get())
    # zip=input("Please enter the zip code you wish to search:")
    base_url="https://www.realtor.com/realestateandhomes-search/"
    r=requests.get(base_url+str(zip), headers=headers)
    c=r.content
    soup=BeautifulSoup(c,"html.parser")
    pg_nr=soup.find_all("a", {"class": "item btn"})[-2].text
    print(pg_nr)


    l=[]
    i=0
    base_url="https://www.realtor.com/realestateandhomes-search/"
    for page in range (1,int(pg_nr),1):
        print(base_url+str(zip)+"/"+"pg-"+str(page))
        r=requests.get(base_url+str(zip)+"/"+"pg-"+str(page), headers=headers)
        c=r.content
        soup=BeautifulSoup(c,"html.parser")
        all=soup.find_all("div", {"class": "property-wrap"})
        for item in all:
            d={}
            try:
                d["Price"]=item.find("span", {"data-label": "pc-price"}).text
                print(item.find("span", {"data-label": "pc-price"}).text)
            except:
                d["Price"] = None
                pass
            try:
                d["Sqft"]=item.find("li", {"data-label": "pc-meta-sqft"}).text
                print(item.find("li", {"data-label": "pc-meta-sqft"}).text)
            except:
                d["Sqft"] = None
                pass
            try:
                d["Sqftlot"]=item.find("li", {"data-label": "pc-meta-sqftlot"}).text
                print(item.find("li", {"data-label": "pc-meta-sqftlot"}).text)
            except:
                d["Sqftlot"] = None
                pass
            try:
                d["Address"] = item.find("div", {"data-label": "pc-address"}).text
                print(item.find("div", {"data-label": "pc-address"}).text)
            except:
                d["Address"] = None
                pass
            try:
                d["Beds"]=item.find("li", {"data-label": "pc-meta-beds"}).text
                print(item.find("li", {"data-label": "pc-meta-beds"}).text)
            except:
                d["Beds"] = None
                pass
            try:
                d["Baths"] = item.find("li", {"data-label": "pc-meta-baths"}).text
                print(item.find("li", {"data-label": "pc-meta-baths"}).text)
            except:
                d["Baths"] = None
                pass
            l.append(d)
            

            

    df=pd.DataFrame(l)
    df
    filename1=str(zip) +" Properties" +".xlsx"
    df.to_excel(filename1)
    t1.insert(END, len(df.index))
    showinfo(message='The Process is completed!')

window = Tk()
window.geometry("800x400")
c=Canvas(window, bg="gray16", height=200, width=200)
window.wm_title("Realtor.com Scraping by Jhangir Awan")
c.pack

l1 = Label(window, text = "Please enter the zip-code you wish to search", font="Raleway")
l1.grid(row=0,column=0)

l2 = Label(window, text = "Properties found:", font="Raleway")
l2.grid(row=0,column=2)

t1 = Text(window, height = 1, width = 20, font="Raleway")
t1.grid(row=0, column=3)

title_text = StringVar()
e1=Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

b1 = Button(window, text = "Download", command = start, font="Raleway", bg="gray16", fg="white", height=2, width=15)
b1.grid(row=1,column=1)




window.mainloop()