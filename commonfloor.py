import requests
from bs4 import BeautifulSoup
import csv  
       
import pandas as pd 



output={}   
output['titles']=[]
output['price']=[]
output['Carpet Area']=[]
output['possession']=[]

output['amenities']=[]
for j in range(1,30):
    URL = "https://www.commonfloor.com/listing-search?city=Bangalore&cg=Bangalore%20division&iscg=&search_intent=sale&polygon=1&page="+str(j)+"&page_size=30"
    print(URL)
    r = requests.get(URL)
    
    soup = BeautifulSoup(r.content, 'html5lib')
    
    name = soup.find_all("div",{"class":"snb-tile-info"})
    
   
    for i  in range(len(name)):
        titles=name[i].find("div",{"class":"st_title"})
        
        tit=titles.h2()
        tit2=tit[0].get_text()
        pri=titles.find("div",{"class":"p_section"})
        if len(pri.select('span'))!=1:
            print(pri.select('span')[1].get_text(strip=True))
            output['price'].append(pri.select('span')[1].get_text(strip=True))
        else:
             print(pri.select('span')[0].get_text(strip=True))
             output['price'].append(pri.select('span')[0].get_text(strip=True))
             
    
        carpet=pri.find("div",{"class":"s_psft"}).get_text(strip=True)
        print(carpet,"+++")
        output['Carpet Area'].append(carpet)
        
        
        possession=name[i].find("div",{"class":"snb-info-dls clearfix"})
        possession1=possession.find_all("div",{"class":"infodata"})[1]
        
    
        print(possession1.find('span').get_text(strip=True))
        output['possession'].append(possession1.find('span').get_text(strip=True))
        
        try:
            amenities=possession.find("ul")
            print(amenities.get_text())
            output['amenities'].append(amenities.get_text(strip=True))
        except:
            print("amenites is empty data")
            output['amenities'].append('')
        output['titles'].append(tit2)
   
df=pd.DataFrame(output)
df.to_csv("commonfloor.csv",index=False)