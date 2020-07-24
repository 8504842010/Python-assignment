import  requests,os
from bs4 import BeautifulSoup

URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
page = requests.get(URL)
#print(page.content)
soup = BeautifulSoup(page.content, 'html.parser')
a=soup.html.text
#print(a)
# print(a.split('\n'))
text = os.linesep.join([s for s in a.splitlines() if s])
print(text)
#print(soup)
#print(soup.find_all('body'))
#x=soup.find_all(('head'))
