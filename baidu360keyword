import requests
try:
  kv={'wd':'daima'}
  r=requests.get("http://www.badu.com/s",params=kv)
  print(r.request.url)
  r.raise_for_status()
  print(len(r.text))
expect:
  print("爬取失败")
