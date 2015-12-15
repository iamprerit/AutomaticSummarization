import re
import operator
def get_sentences(fno,sum_sen):
	text_string=(open("article_text"+fno+".txt","r").read())
	text_heading=(open("article_headline"+fno+".txt","r").read())
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
	sc={}
	for s in sentence_list:
		sc[i+1]=score_sentence(s,i,text_heading,text_string,len(sentence_list))
		i=i+1
	sorted_x = sorted(sc.items(), key=operator.itemgetter(1),reverse=True)
	final=sorted(sorted_x[0:sum_sen])
	with open("article_summarized"+fno+".txt",'w') as f:
		f.write(text_heading+"\n")
		for x in final:
			#print(x[0])
			f.write(sentence_list[x[0]-1])
	return


def score_sentence(sen,sno,heading,text,totsen):
	stopWords=getStopWordList()
	sen=sen.lower()
	sen_words=sen.split()
	for w in sen_words:
		if w in stopWords:
			sen_words.remove(w)
	heading=heading.lower()
	heading_words=heading.split()
	for w in heading_words:
		if w in stopWords:
			heading_words.remove(w)
	s1=word_freq_score(sen_words,text.lower())
	s2=sentence_position_score(sno,totsen)
	s3=title_feature_score(sen_words,heading_words)
	ts=((s1*2.0)+(s2*1.0)+(s3*1.5))/3
	return ts
def word_freq_score(words,text):
	text_list=text.split()
	sum=0
	for x in words:
		sum+=text_list.count(x)
	#print(sum)
	return sum
def title_feature_score(sen,head):
	cnt=0
	for x in sen:
		if x in head:
			cnt+=1

	cnt=cnt*1.0
	cnt=cnt/len(head)
	return cnt
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
def sentence_position_score(i, size):
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
if __name__ == '__main__':
	get_sentences("3",5)