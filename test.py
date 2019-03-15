import requests
url="http://www.ip138.com/ips138.asp?ip="
try :
        r=requests.get(url+'117.89.193.221')
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        print(r.text[-5000:])
except:
        print("爬取失败")
