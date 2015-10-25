from .twitter import TwitterMood

def Coordinator():
	return None

def NewResult(twitter_query, twitter_sid):
	new_result = []
#----------------------twitter-engine--------------------------------------#
	(twi_result, new_twitter_sid) = TwitterMood(twitter_query, twitter_sid)
#----------------------twitter-engine--------------------------------------#
# more engines will be available...

	if(len(twi_result) > 0):
		new_result += twi_result
		return(new_result, new_twitter_sid)
	else:
		return(new_result, twitter_sid)

