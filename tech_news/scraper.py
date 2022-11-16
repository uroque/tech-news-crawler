import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        response = requests.get(
            url,
            timeout=3,
            headers={"user-agent": "Fake user-agent"}
        )
        response.raise_for_status()
        time.sleep(1)
    except (requests.HTTPError, requests.ReadTimeout):
        return None
    return response.text


# Requisito 2
def scrape_novidades(html_content):
    css_to_parse = "a.cs-overlay-link::attr(href)"
    news_href = Selector(html_content).css(css_to_parse).getall()
    return news_href


# Requisito 3
def scrape_next_page_link(html_content):
    css_to_parse = "a.next::attr(href)"
    return Selector(html_content).css(css_to_parse).get()


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
