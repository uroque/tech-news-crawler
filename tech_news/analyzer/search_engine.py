from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    query = {"title": {"$regex": title, "$options": "i"}}
    return [(news["title"], news["url"]) for news in search_news(query)]


# Requisito 7
def search_by_date(date):
    format = "%d/%m/%Y"

    try:
        formated_date = datetime.strptime(date, "%Y-%m-%d").strftime(format)
        query = {"timestamp": {"$eq": formated_date}}
    except ValueError:
        raise ValueError("Data inválida")
    return [(news["title"], news["url"]) for news in search_news(query)]


# Requisito 8
def search_by_tag(tag):
    query = {'tags': {'$regex': tag, '$options': 'i'}}
    return [(news['title'], news['url']) for news in search_news(query)]


# Requisito 9
def search_by_category(category):
    query = {"category": {"$regex": category, "$options": "i"}}
    return [(news['title'], news['url']) for news in search_news(query)]
