"""
Bitcoin Price Alert System
Monitors BTC price changes and sends SMS notifications with relevant news
"""

import requests
from twilio.rest import Client
from datetime import datetime
from config import (
    NEWS_API_KEY,
    TWILIO_ACCOUNT_SID,
    TWILIO_AUTH_TOKEN,
    TWILIO_FROM_NUMBER,
    TWILIO_TO_NUMBER
)

# Configuration
STOCK_NAME = "BTC"
COMPANY_NAME = "Bitcoin"
PRICE_CHANGE_THRESHOLD = 1.0  # Alert if price changes by more than 1%

# API Endpoints
CRYPTO_ENDPOINT = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


def get_bitcoin_price():
    """Fetch Bitcoin price data for the last 2 days"""
    print("📊 Fetching Bitcoin price data...")
    
    params = {
        "vs_currency": "usd",
        "days": "2",
        "interval": "daily"
    }
    
    response = requests.get(CRYPTO_ENDPOINT, params=params)
    response.raise_for_status()
    data = response.json()
    
    prices = data["prices"]
    yesterday_price = float(prices[-1][1])
    day_before_price = float(prices[-2][1])
    
    return yesterday_price, day_before_price


def calculate_price_change(current_price, previous_price):
    """Calculate the percentage change between two prices"""
    difference = abs(current_price - previous_price)
    percentage_change = (difference / current_price) * 100
    direction = "UP" if current_price > previous_price else "DOWN"
    
    return difference, percentage_change, direction


def fetch_bitcoin_news():
    """Fetch the latest Bitcoin news articles"""
    print("📰 Fetching Bitcoin news...")
    
    params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": 3
    }
    
    response = requests.get(NEWS_ENDPOINT, params=params)
    response.raise_for_status()
    articles = response.json().get("articles", [])
    
    return articles[:3]


def format_articles(articles, current_price):
    """Format news articles for SMS"""
    if len(articles) > 0:
        return [
            {
                "title": article.get("title", "No title")[:100],
                "description": article.get("description", "No description")[:150],
            }
            for article in articles
        ]
    else:
        return [{
            "title": "Bitcoin Price Update",
            "description": f"Current price: ${current_price:,.2f}"
        }]


def send_sms_alerts(articles, price_info):
    """Send SMS notifications via Twilio"""
    print("📱 Sending SMS alerts...")
    
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    percent_text = f"{STOCK_NAME} {price_info['direction']} {price_info['percentage']:.2f}%"
    
    messages_sent = 0
    
    for i, article in enumerate(articles, 1):
        message_body = (
            f"{percent_text}\n"
            f"Headline: {article['title']}\n"
            f"Brief: {article['description']}"
        )
        
        try:
            msg = client.messages.create(
                body=message_body,
                from_=TWILIO_FROM_NUMBER,
                to=TWILIO_TO_NUMBER,
            )
            print(f"✅ Message {i} sent! SID: {msg.sid}")
            messages_sent += 1
        except Exception as e:
            print(f"❌ Error sending message {i}: {e}")
    
    return messages_sent


def main():
    """Main execution function"""
    try:
        # Get price data
        yesterday_price, day_before_price = get_bitcoin_price()
        
        print(f"💰 Yesterday: ${yesterday_price:,.2f}")
        print(f"💰 Day before: ${day_before_price:,.2f}")
        
        # Calculate price change
        difference, percentage, direction = calculate_price_change(
            yesterday_price, 
            day_before_price
        )
        
        print(f"📈 Change: ${difference:,.2f} ({percentage:.2f}%)")
        
        # Check if alert threshold is met
        if percentage > PRICE_CHANGE_THRESHOLD:
            print(f"⚠️ Price change exceeds {PRICE_CHANGE_THRESHOLD}% threshold!")
            
            # Fetch news
            articles = fetch_bitcoin_news()
            print(f"📰 Found {len(articles)} articles")
            
            # Format articles
            formatted_articles = format_articles(articles, yesterday_price)
            
            # Send SMS alerts
            price_info = {
                'direction': direction,
                'percentage': percentage,
                'difference': difference
            }
            
            messages_sent = send_sms_alerts(formatted_articles, price_info)
            
            print(f"✅ Successfully sent {messages_sent} SMS alerts!")
        else:
            print(f"ℹ️ Price change ({percentage:.2f}%) below threshold ({PRICE_CHANGE_THRESHOLD}%)")
            print("No alerts sent.")
        
        print(f"\n✅ Script completed at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
    except Exception as e:
        print(f"❌ Fatal error: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()