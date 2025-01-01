from django.shortcuts import render
from newsapi import NewsApiClient

def index(req):
    newsApi = NewsApiClient(api_key='e507908f74b14e7da3d5dd0127f7b3c6')
    
    # Get headlines from multiple sources
    sources = ["breitbart-news",'reuters','bbc-news', 'abc-news']
    articles = []
    
    for source in sources:
        headlines = newsApi.get_top_headlines(sources=source)
        if headlines['articles']:
            articles.extend(headlines['articles'])

    desc = []
    news = []
    img = []

    for article in articles:
        desc.append(article.get('description', ''))
        news.append(article.get('title', ''))
        img.append(article.get('urlToImage', ''))

    mylist = zip(news, desc, img)
    return render(req, "main/index.html", context={"mylist": mylist})