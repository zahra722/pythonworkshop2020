import requests 
from requests_html import HTMLSession
session = HTMLSession()
r = session.get("https://www.imdb.com/title/tt1187043/")

lister = r.html.find('.title_block',first=True)
print(lister.text)
# Title = lister.find('.article .titlecast')
#rating = lister.find('.overview-top')
#print(type(rating))

# for i in range(0,len(Title)):

#     print(Title[i].text)
    #print(rating[i].text)

#img = lister.find('.posterColumn a img')

#req = requests.get("https://www.instagram.com/")
#print(req.text)
#print(req.text[0:500])
#print(req.encoding)
#print(req.status_code)
#print(req.elapsed)
#print(req.url)