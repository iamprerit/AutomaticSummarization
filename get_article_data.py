from bs4 import BeautifulSoup
from urllib.request import urlopen
def get_article_links(section_url):
	BASE_URL="http://timesofindia.indiatimes.com"
	html=urlopen(section_url).read()
	soup=BeautifulSoup(html,"lxml")
	article_grab=soup.find("div","top-story")
	article_links = [" "+BASE_URL + li.a["href"]+" " for li in article_grab.findAll("li")]
	f=open("article_links.txt",'w')
	for x in article_links[0:4]:
		f.write(x+'\n')
	f.close()
	return 
if __name__ == '__main__':
	get_article_links("http://timesofindia.indiatimes.com")





