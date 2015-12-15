from bs4 import BeautifulSoup
from urllib.request import urlopen
def get_article_text():
	with open("article_links.txt","r") as f:
		links=f.readlines()
	i=1;
	for x in links:
		real_text(x,i)
		i=i+1
	return
def real_text(site_url,n):
	html=urlopen(site_url).read()
	soup=BeautifulSoup(html,'lxml')
	headline=soup.find("h1","heading1").string
	text_grab=soup.find("div","section1")
	f1=open("article_headline"+str(n)+".txt",'w')
	f2=open("article_text"+str(n)+".txt",'w')
	f1.write(headline+"\n")
	f2.write(text_grab.text)
	f1.close()
	f2.close()
	return 
if __name__ == '__main__':
	get_article_text()





