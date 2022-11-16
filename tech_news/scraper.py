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
    selector = Selector(html_content)
    return {
        "url": selector.css("[rel='canonical']::attr(href)").get(),
        "title": selector.css(".entry-title::text").get().strip(),
        "timestamp": selector.css(".meta-date::text").get(),
        "writer": selector.css(".author a.url::text").get(),
        "category": selector.css(".category-style span.label::text").get(),
        "comments_count": len(selector.css(".comment-list li").getall()),
        "tags": selector.css("a[rel='tag']::text").getall(),
        "summary": "".join(
            selector.css(".entry-content > p:nth-of-type(1) ::text").getall()
        ).strip(),
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
