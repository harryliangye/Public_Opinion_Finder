from django.shortcuts import render
from django.http import HttpResponse
from textblob import TextBlob

def SentimentTool(request):
	if(request.method == 'POST'):
		content_tb = TextBlob(request.POST['text'])
		return render(request,'Sentiment/SentimentTool.html',{'sentiment':content_tb.polarity})
	else:
		return render(request,'Sentiment/SentimentTool.html',{'sentiment':None})


# Create your views here.
