# Developed and modified by Ye Liang at 15:21 Oct,25 2015
# All rights reserved
from .twitter import TwitterMood
from .filter import TwitterFilter
def Coordinator():
	return None

def NewResult(twitter_query, twitter_sid, result_count):
	new_result = []

	new_twitter_sid = twitter_sid
	while(len(new_result) < result_count):
#----------------------twitter-engine--------------------------------------#
		(twi_result, new_twitter_sid) = TwitterMood(twitter_query, new_twitter_sid)
#------------------------------filter--------------------------------------#
		if(len(twi_result) > 0):
			ntwitter_result = TwitterFilter(twi_result)
			if(len(ntwitter_result) > 0):
				new_result += ntwitter_result
		else:
			break
#------------------------------filter--------------------------------------#
#----------------------twitter-engine--------------------------------------#
# more engines will be available...

	return(new_result, new_twitter_sid)

