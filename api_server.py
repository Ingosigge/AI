import requests
import pandas as pd
from flask import Flask, jsonify
import logging

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
            for article in data.get("articles", [])
        ]
        return articles
    except Exception as e:
        logger.error(f"Error fetching Google News: {e}")
        return []

@app.route('/api/trends', methods=['GET'])
def get_trends():
    logger.info("Fetching AI trends...")
    news_data = fetch_google_news()
    df_news = pd.DataFrame(news_data)
    
    if df_news.empty:
        return jsonify({"error": "No data available"}), 500
    
    return jsonify(df_news.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
