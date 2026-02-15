# 📈 Bitcoin Price Alert System

An automated cryptocurrency monitoring system that tracks Bitcoin price changes and sends real-time SMS notifications with relevant market news.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

## 🎯 Features

- **Real-time Price Tracking**: Monitors Bitcoin price changes using CoinGecko API
- **Smart Alerts**: Sends SMS notifications when price changes exceed threshold
- **News Integration**: Automatically fetches and includes relevant Bitcoin news
- **Configurable**: Customizable price change thresholds
- **Error Handling**: Robust error handling and logging
- **Secure**: Uses environment variables for API keys

## 🛠️ Tech Stack

- **Language**: Python 3.8+
- **APIs**:
  - CoinGecko API (cryptocurrency price data)
  - NewsAPI (market news)
  - Twilio API (SMS notifications)
- **Libraries**: `requests`, `twilio`, `python-dotenv`



### Terminal Output
```
📊 Fetching Bitcoin price data...
💰 Yesterday: $45,234.67
💰 Day before: $43,891.23
📈 Change: $1,343.44 (2.97%)
⚠️ Price change exceeds 1.0% threshold!
📰 Fetching Bitcoin news...
📰 Found 3 articles
📱 Sending SMS alerts...
✅ Message 1 sent! SID: SM1234...
✅ Message 2 sent! SID: SM5678...
✅ Message 3 sent! SID: SM9012...
✅ Successfully sent 3 SMS alerts!
```

### SMS Alert Example
```
BTC UP 2.97%
Headline: Bitcoin Surges Past $45K...
Brief: Bitcoin price rallied today...
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Twilio account (free trial works)
- NewsAPI key (free tier available)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/bitcoin-alert-system.git
cd bitcoin-alert-system
```

2. **Create virtual environment**
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
```bash
# Copy the example file
cp .env.example .env

# Edit .env and add your API keys:
# - Get NewsAPI key from: https://newsapi.org/register
# - Get Twilio credentials from: https://console.twilio.com/
```

5. **Run the script**
```bash
python main.py
```

## ⚙️ Configuration

### Environment Variables

Create a `.env` file with the following variables:

```env
NEWS_API_KEY=your_news_api_key
TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_token
TWILIO_FROM_NUMBER=+1234567890
TWILIO_TO_NUMBER=+1234567890
```

### Price Threshold

Modify the threshold in `main.py`:

```python
PRICE_CHANGE_THRESHOLD = 1.0  # Alert if price changes by more than 1%
```

## 📊 How It Works

1. **Fetch Price Data**: Retrieves Bitcoin prices for the last 2 days from CoinGecko
2. **Calculate Change**: Computes the percentage change between closing prices
3. **Check Threshold**: Compares change against configured threshold
4. **Fetch News**: If threshold exceeded, fetches latest Bitcoin news
5. **Send Alerts**: Sends formatted SMS messages via Twilio

## 🎓 What I Learned

This project helped me understand:

- **REST API Integration**: Working with multiple third-party APIs
- **Error Handling**: Implementing robust error handling for network requests
- **Rate Limit Management**: Dealing with API rate limits and quotas
- **Environment Variables**: Securely managing API keys and credentials
- **Code Organization**: Writing clean, modular, maintainable code
- **Real-time Data Processing**: Handling and analyzing live market data

## 🔮 Future Improvements

- [ ] Support for multiple cryptocurrencies (ETH, SOL, etc.)
- [ ] Email notifications as alternative to SMS
- [ ] Web dashboard with historical price charts
- [ ] Database integration for price history
- [ ] Machine learning price prediction model
- [ ] Telegram bot integration
- [ ] Docker containerization
- [ ] Automated testing suite

## 📝 Project Structure

```
bitcoin-alert-system/
├── main.py              # Main application script
├── requirements.txt     # Python dependencies
├── .env.example        # Environment variables template
├── .gitignore          # Git ignore rules
└── README.md           # Project documentation
```

## ⚠️ Important Notes

- **Twilio Trial**: Free trial accounts can only send SMS to verified numbers
- **API Limits**: 
  - CoinGecko: 50 calls/minute (free tier)
  - NewsAPI: 100 requests/day (free tier)
  - Twilio: Check your account limits
- **Security**: Never commit `.env` file or expose API keys

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the project
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

**Your Name**
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourprofile)
- GitHub: [@yourusername](https://github.com/yourusername)
- Email: your.email@example.com

## 🙏 Acknowledgments

- [CoinGecko](https://www.coingecko.com/) for cryptocurrency data
- [NewsAPI](https://newsapi.org/) for news aggregation
- [Twilio](https://www.twilio.com/) for SMS infrastructure

---

⭐ If you found this project helpful, please give it a star!
