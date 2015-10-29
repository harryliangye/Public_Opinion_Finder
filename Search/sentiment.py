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
		ite = 0
		for content in content_list:
			i = 10 - int((1000 - ite) / 100)
			print(i)
			if content.polarity > 0:
				pos += 1
			elif content.polarity < 0:
				neg += 1
			else:
				neu += 1
			polar_score[i] += content.polarity
			sub_score[i] += content.subjectivity
			ite += 1
		return_type = [pos, neg, neu, polar_score, sub_score]
		return(return_type)
	else:
		return None
