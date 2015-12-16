import os
import extract_sentences
import get_article_data
import get_text
def driver():
	os.system("dialog --backtitle 'by @iamprerit' --title 'Automatic Text Summarisation' --shadow --msgbox 'Press OK to proceed' 7 30")
	os.system("dialog --backtitle 'by @iamprerit' --title 'Automatic Text Summarisation' --shadow --msgbox 'Top 4 Articles from TOI website would be summarised in 5 sentences' 7 30 ")
	os.system("dialog --backtitle 'by @iamprerit' --title 'Automatic Text Summarisation' --shadow --nook --msgbox 'Program in progress...please wait(Press OK)' 7 30")
	get_article_data.get_article_links("http://timesofindia.indiatimes.com")
	get_text.get_article_text()
	for x in ['1','2','3','4']:
		extract_sentences.get_sentences(x,5)
	os.system("dialog --backtitle 'by @iamprerit' --title 'Automatic Text Summarisation' --shadow --msgbox 'Summarisation Complete. Kindly check the files' 7 30")
	return
if __name__ == '__main__':
	driver()