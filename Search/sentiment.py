from textblob import TextBlob

def SentimentAnalyzer(content_list):
	count = 0
	for content in content_list:
		tb_content = TextBlob(content.text)
		content.polarity = tb_content.polarity
		content.subjectivity = tb_content.subjectivity
		count += 1
	return count

def SentimentAnalyzer1000(content_list):
	if len(content_list) >= 1000:
		pos = 0
		neg = 0
		neu = 0
		polar_score = [0,0,0,0,0,0,0,0,0,0,0]
		sub_score = [0,0,0,0,0,0,0,0,0,0,0]
		sentiment_list = []
		score_sequence = []
		ite = 1
		for content in content_list:
			if (ite > 1000):
				break
			i = 10 - int((1000 - ite) / 100)
			if content.polarity > 0:
				pos += 1
			elif content.polarity < 0:
				neg += 1
			else:
				neu += 1
			sentiment_list.append([content.subjectivity,content.polarity])#subjectivity,polarization
			polar_score[i] += content.polarity
			sub_score[i] += content.subjectivity
			ite += 1
		for ind in range(1,11):
			score_sequence.append(round(sub_score[ind]/100, 2))#instead of ind-1
			score_sequence.append(round(polar_score[ind]/100, 2))
		return_type = [pos, neg, neu, round(sum(polar_score)/len(content_list),2), 
						round(sum(sub_score)/len(content_list),2), score_sequence, sentiment_list]
		# gauge_data1: return_type[3] gauge_data2: return_type[4] curve:[5] scatter:return_type[6], 
		return(return_type)
	else:
		return None
