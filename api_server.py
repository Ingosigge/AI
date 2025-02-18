import requests
import pandas as pd
from flask import Flask, jsonify
import logging
import os

# Konfiguration för API-nycklar (lägg in dina egna nycklar här)
GOOGLE_NEWS_API_KEY = "din_google_news_api_key"

# Initiera Flask-app
app = Flask(__name__)

# Konfigurera logging för att felsöka problem
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Funktion för att hämta AI-relaterade nyheter från Google News
def fetch_google_news():
    try:
        url = f"https://newsapi.org/v2/everything?q=AI+leadership+OR+AI+management&sortBy=publishedAt&apiKey={GOOGLE_NEWS_API_KEY}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        articles = [
            {
                "source": article["source"]["name"],
                "title": article["title"],
                "url": article["url"],
                "published": article["publishedAt"],
                "content": article.get("content", "")
            }
            for article in data.get("articles
