from django.shortcuts import render
from newsapi import NewsApiClient

def index(request):
    # Initialize the News API client
    newsapi = NewsApiClient(api_key='YourAPIkey')
    
    # Fetch news articles from 'techcrunch'
    articles = newsapi.get_everything(sources='techcrunch')['articles']
    
    # Render the 'index.html' template with the articles
    return render(request, 'index.html', context={"articles": articles})
