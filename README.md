# 🤖 Metis - Your AI-Powered Financial Sidekick!

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://python.org)
[![VS Code](https://img.shields.io/badge/IDE-VS%20Code-blue.svg)](https://code.visualstudio.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)]()

> **Week 1 Assignment**: Build a Cryptocurrency Advisor Chatbot  
> **Theme**: *"Your First AI-Powered Financial Sidekick!"* 🌟

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Chatbot Capabilities](#chatbot-capabilities)
- [Sample Conversations](#sample-conversations)
- [Technical Details](#technical-details)
- [Screenshots](#screenshots)
- [Assignment Reflection](#assignment-reflection)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [Disclaimer](#disclaimer)

## 🎯 Overview

**Metis** is an intelligent rule-based chatbot that analyzes cryptocurrency data and provides investment advice based on **profitability** (price trends, market cap) and **sustainability** (energy efficiency, environmental impact). Built for Gen Z investors, especially those in Africa, this chatbot combines friendly conversation with data-driven insights.

### 🎨 Chatbot Personality
- **Name**: Metis (Named after the Greek goddess of wisdom and deep thought)
- **Tone**: Friendly, encouraging, and meme-loving
- **Target Audience**: Gen Z crypto beginners
- **Focus**: Education over speculation

## ✨ Features

### 🔍 **Smart Analysis**
- Cryptocurrency trend analysis
- Sustainability scoring (1-10 scale)
- Energy consumption evaluation
- Risk assessment

### 💬 **Conversational Interface**
- Natural language processing
- Context-aware responses
- Personalized recommendations
- Interactive help system

### 🌱 **Sustainability Focus**
- Environmental impact assessment
- Energy-efficient coin recommendations
- Green investing guidance

### 📊 **Investment Insights**
- Profitability analysis
- Market cap comparisons
- Risk level evaluation
- Trend identification

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- No external libraries required (uses only built-in Python modules)

### Quick Start
1. **Clone the repository**
   ```bash
   git clone https://github.com/[your-username]/metis-crypto-advisor.git
   cd metis-crypto-advisor
   ```

2. **Open in VS Code**
   ```bash
   code .
   ```

3. **Run the chatbot**
   - Open integrated terminal in VS Code (`Ctrl+` ` or `View > Terminal`)
   - Run: `python metis.py`

4. **Start chatting!**
   ```
   Metis: Hey there! 🚀 Let's find you a green and growing crypto!
   ```

## 💻 Usage

### Running in VS Code (Recommended)

#### **Method 1: Integrated Terminal**
1. Open VS Code
2. Open the project folder
3. Open integrated terminal (`Ctrl+` ` )
4. Run: `python metis.py`

#### **Method 2: Run Python File**
1. Open `metis.py` in VS Code
2. Right-click in the editor
3. Select "Run Python File in Terminal"

#### **Method 3: Code Runner Extension**
1. Install Code Runner extension
2. Open `metis.py`
3. Press `Ctrl+F5` or click the ▶️ button

## 🧠 Chatbot Capabilities

### 🔥 **Profitability Queries**
- `"What's trending?"` → Find rising cryptocurrencies
- `"Most profitable coin?"` → Get profit-focused recommendations
- `"Market cap leaders?"` → See high market cap coins

### 🌱 **Sustainability Queries**
- `"Most sustainable crypto?"` → Find eco-friendly options
- `"Green investments?"` → Get low-energy recommendations
- `"Environmental impact?"` → Learn about energy usage

### 📊 **Comparison & Analysis**
- `"Compare Bitcoin Ethereum"` → Side-by-side analysis
- `"Info about Cardano"` → Detailed coin information
- `"Show all coins"` → Complete cryptocurrency list

### 🎯 **Personalized Advice**
- `"Best recommendation?"` → Balanced advice
- `"What should I invest in?"` → Personalized suggestions

## 🗣️ Sample Conversations

### Example 1: Sustainability Focus
```
You: Which crypto is most sustainable?
Metis: 🌱 Polygon (MATIC) is your greenest choice!

📊 Sustainability Score: 9/10
⚡ Energy Use: Very Low
📈 Price Trend: Rising
💡 Why: Ethereum scaling solution with low fees

Perfect for eco-conscious investors who care about the planet! 🌍
```

### Example 2: Profitability Analysis
```
You: What's trending up?
Metis: 🚀 Bitcoin (BTC) looks promising for profits!

📈 Trend: Rising 
💰 Market Cap: High
⚠️ Risk Level: Medium
💡 About: The original cryptocurrency, digital gold

Great momentum for potential gains! 📊
```

### Example 3: Coin Comparison
```
You: Compare Bitcoin Cardano
Metis: 🆚 Bitcoin vs Cardano COMPARISON

📊 Bitcoin (BTC)
   └─ Price Trend: Rising
   └─ Market Cap: High
   └─ Sustainability: 3/10
   └─ Energy Use: High

📊 Cardano (ADA)
   └─ Price Trend: Rising
   └─ Market Cap: Medium
   └─ Sustainability: 8/10
   └─ Energy Use: Low

🏆 Winner for Sustainability: Cardano
💰 Better Market Position: Bitcoin
```

## 🔧 Technical Details

### **Architecture**
- **Language**: Python 3.7+
- **Design Pattern**: Rule-based chatbot with class-based structure
- **Data Storage**: In-memory dictionary (no external database required)
- **NLP**: Simple keyword matching and pattern recognition

### **Key Components**

#### **Metis Class**
```python
class Metis:
    - __init__(): Initialize chatbot and crypto database
    - process_user_input(): Handle user queries with rule-based logic
    - get_sustainable_recommendation(): Find eco-friendly coins
    - get_profitable_recommendation(): Identify profitable opportunities
    - compare_cryptocurrencies(): Side-by-side coin analysis
```

#### **Cryptocurrency Database**
```python
crypto_db = {
    "Bitcoin": {
        "symbol": "BTC",
        "price_trend": "rising",
        "market_cap": "high", 
        "energy_use": "high",
        "sustainability_score": 3,
        "risk_level": "medium"
    },
    # ... more cryptocurrencies
}
```

### **Decision-Making Logic**

#### **Sustainability Scoring**
- **9-10**: Excellent (Very low energy, proof-of-stake)
- **7-8**: Good (Low energy consumption)
- **4-6**: Fair (Medium energy usage)
- **1-3**: Poor (High energy consumption)

#### **Profitability Analysis**
```python
if "sustainable" in user_query:
    recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
    return f"Invest in {recommend}! 🌱 It's eco-friendly!"

if "trending" in user_query:
    rising_coins = [coin for coin, data in crypto_db.items() 
                   if data["price_trend"] == "rising"]
    return f"These coins are trending: {rising_coins}"
```

## 📸 Screenshots

### Main Interface
```
🤖 METIS - YOUR AI CRYPTO ADVISOR 🤖
==================================================
💡 I analyze crypto based on profitability & sustainability!
🌱 Ask me about trends, sustainable coins, or investment advice!
⚠️  Remember: Crypto is risky—always do your own research!
==================================================

Metis: Hey there! 🚀 Let's find you a green and growing crypto!
Metis: What's your name, future crypto investor?
```

### Help Menu
```
🆘 METIS HELP MENU 🆘
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💰 PROFITABILITY QUERIES:
   • "trending" or "rising" - Find coins with upward price trends
   • "profitable" or "gains" - Get profitability-focused recommendations

🌱 SUSTAINABILITY QUERIES:
   • "sustainable" or "eco" - Find environmentally friendly coins
   • "green" or "clean" - Get low-energy consumption recommendations
```━━━━━━━━━━━━━━━━━━━
💰 PROFITABILITY QUERIES:
   • "trending" or "rising" - Find coins with upward price trends
   • "profitable" or "gains" - Get profitability-focused recommendations

🌱 SUSTAINABILITY QUERIES:
   • "sustainable" or "eco" - Find environmentally friendly coins
   • "green" or "clean" - Get low-energy consumption recommendations
```

## 🤔 Assignment Reflection

### **How does this chatbot mimic basic AI decision-making?**

CryptoBuddy demonstrates fundamental AI decision-making through rule-based logic that processes user input, analyzes cryptocurrency data against multiple criteria (profitability and sustainability), and provides contextual recommendations. The bot uses pattern matching to understand user intent, applies weighted scoring algorithms to rank cryptocurrencies, and generates personalized responses based on data-driven analysis—mimicking how AI systems evaluate options and make informed decisions.

### **Key Learning Outcomes**
✅ **AI-driven decision-making**: Implemented logic trees for investment recommendations  
✅ **Conversational design**: Created engaging, personality-driven interactions  
✅ **Data analysis**: Built scoring algorithms for crypto evaluation  
✅ **User experience**: Designed intuitive help systems and error handling  

## 🚀 Future Enhancements

### **Stretch Goals Implemented**
- ✅ Enhanced personality and conversational flow
- ✅ Comprehensive help system
- ✅ Risk assessment features
- ✅ Detailed comparison tools

### **Potential Improvements**
- 🔄 **API Integration**: Real-time data from CoinGecko API
- 🧠 **NLP Enhancement**: Natural Language Toolkit (NLTK) integration  
- 📱 **Mobile Interface**: WhatsApp/Telegram bot deployment
- 📊 **Data Visualization**: Charts and graphs for trend analysis
- 🌍 **Localization**: Multi-language support for African markets

## 🤝 Contributing
