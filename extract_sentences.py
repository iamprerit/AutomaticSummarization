import re
def get_sentences():
	text_string=(open("article_text4.txt","r").read())
	text_heading=(open("article_headline4.txt","r").read())
	text_string=re.sub(r'[\s]+',' ',text_string)
	text_string=re.sub(r'\s--\s',' ',text_string)
	text_string=re.sub(r'\s\.\.\s?',' ',text_string)
	text_string=re.sub(r'\\\'','\'',text_string)
	sentence_list=re.split(r'\s?[\.]\s',text_string)
	for x in sentence_list:
		if len(x)<=3:
			sentence_list.remove(x)
			continue
	i=0
	sc=[]#score array for particular text
	for s in sentence_list:
		sc.append(score_sentence(s,i,text_heading))
		i+=1
	return	
def score_sentence(sen,i,heading):
	stopWords=getStopWordList()
	sen=sen.lower()
	words=sen.split()
	for w in words:
		if w in stopWords:
			words.remove(w)
	# word_freq(w)
	# sentence_position(w,i)
	# title_feature(w,heading)
	return
def getStopWordList():
	stopWords = []
	fp = open("stopWordsFile.txt", 'r')
	line = fp.readline()
	while line:
		word = line.strip()
		stopWords.append(word)
		line = fp.readline()
	fp.close()
	return stopWords
def sentence_position(i, size):
    normalized = i*1.0 / size
    if 0 < normalized <= 0.1:
        return 0.17
    elif 0.1 < normalized <= 0.2:
        return 0.23
    elif 0.2 < normalized <= 0.3:
        return 0.14
    elif 0.3 < normalized <= 0.4:
        return 0.08
    elif 0.4 < normalized <= 0.5:
        return 0.05
    elif 0.5 < normalized <= 0.6:
        return 0.04
    elif 0.6 < normalized <= 0.7:
        return 0.06
    elif 0.7 < normalized <= 0.8:
        return 0.04
    elif 0.8 < normalized <= 0.9:
        return 0.04
    elif 0.9 < normalized <= 1.0:
        return 0.15
    else:
        return 0

get_sentences()