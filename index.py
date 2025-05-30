#!/usr/bin/env python3
"""
Metis - Your AI-Powered Financial Sidekick! 🌟
A rule-based cryptocurrency advisor chatbot that provides investment advice
based on profitability and sustainability metrics.

Author: [Your Name]
Date: May 2025
Assignment: Week 1 - Build a Cryptocurrency Advisor Chatbot
IDE: VS Code
"""

import random
import time

class Metis:
    def __init__(self):
        self.name = "Metis"
        # Predefined cryptocurrency database
        self.crypto_db = {
            "Bitcoin": {
                "symbol": "BTC",
                "price_trend": "rising",
                "market_cap": "high",
                "energy_use": "high",
                "sustainability_score": 3,
                "risk_level": "medium",
                "description": "The original cryptocurrency, digital gold"
            },
            "Ethereum": {
                "symbol": "ETH",
                "price_trend": "stable",
                "market_cap": "high",
                "energy_use": "medium",
                "sustainability_score": 6,
                "risk_level": "medium",
                "description": "Smart contract platform with wide adoption"
            },
            "Cardano": {
                "symbol": "ADA",
                "price_trend": "rising",
                "market_cap": "medium",
                "energy_use": "low",
                "sustainability_score": 8,
                "risk_level": "medium",
                "description": "Proof-of-stake blockchain focused on sustainability"
            },
            "Solana": {
                "symbol": "SOL",
                "price_trend": "volatile",
                "market_cap": "medium",
                "energy_use": "low",
                "sustainability_score": 7,
                "risk_level": "high",
                "description": "Fast blockchain for DeFi and NFTs"
            },
            "Polygon": {
                "symbol": "MATIC",
                "price_trend": "rising",
                "market_cap": "medium",
                "energy_use": "very_low",
                "sustainability_score": 9,
                "risk_level": "medium",
                "description": "Ethereum scaling solution with low fees"
            }
        }
        
        # Greeting messages
        self.greetings = [
            "Hey there! 🚀 Let's find you a green and growing crypto!",
            "Welcome to Metis! 💰 Your AI financial sidekick is here!",
            "Hi! Ready to explore the crypto universe together? 🌟",
            "Greetings, crypto explorer! Let's make some smart investment decisions! 💎"
        ]
        
        # Initialize conversation
        self.conversation_active = True
        self.user_name = None

    def display_banner(self):
        """Display welcome banner"""
        print("=" * 50)
        print("🤖 METIS - YOUR AI CRYPTO ADVISOR 🤖")
        print("=" * 50)
        print("💡 I analyze crypto based on profitability & sustainability!")
        print("🌱 Ask me about trends, sustainable coins, or investment advice!")
        print("⚠️  Remember: Crypto is risky—always do your own research!")
        print("=" * 50)
        print()

    def greet_user(self):
        """Greet the user and get their name"""
        greeting = random.choice(self.greetings)
        print(f"Metis: {greeting}")
        print("Metis: What's your name, future crypto investor?")
        
        self.user_name = input("You: ").strip()
        if self.user_name:
            print(f"Metis: Nice to meet you, {self.user_name}! 🎉")
        else:
            self.user_name = "Friend"
            print("Metis: Nice to meet you, Friend! 🎉")
        
        print("Metis: Type 'help' to see what I can do, or 'quit' to exit!")
        print()

    def show_help(self):
        """Display available commands"""
        help_text = """
🆘 METIS HELP MENU 🆘
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💰 PROFITABILITY QUERIES:
   • "trending" or "rising" - Find coins with upward price trends
   • "profitable" or "gains" - Get profitability-focused recommendations
   • "market cap" - Learn about market capitalization

🌱 SUSTAINABILITY QUERIES:
   • "sustainable" or "eco" - Find environmentally friendly coins
   • "green" or "clean" - Get low-energy consumption recommendations
   • "energy" - Learn about energy usage

📊 GENERAL QUERIES:
   • "compare [coin1] [coin2]" - Compare two cryptocurrencies
   • "info [coin]" - Get detailed information about a specific coin
   • "all coins" - See all available cryptocurrencies
   • "best" or "recommend" - Get personalized recommendations

🛠️ COMMANDS:
   • "help" - Show this menu
   • "quit" or "exit" - End conversation
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        """
        print(help_text)

    def get_sustainable_recommendation(self):
        """Find the most sustainable cryptocurrency"""
        best_crypto = max(self.crypto_db.keys(), 
                         key=lambda x: self.crypto_db[x]["sustainability_score"])
        
        data = self.crypto_db[best_crypto]
        return f"""🌱 **{best_crypto} ({data['symbol']})** is your greenest choice!
        
📊 Sustainability Score: {data['sustainability_score']}/10
⚡ Energy Use: {data['energy_use'].replace('_', ' ').title()}
📈 Price Trend: {data['price_trend'].title()}
💡 Why: {data['description']}

Perfect for eco-conscious investors who care about the planet! 🌍"""

    def get_profitable_recommendation(self):
        """Find cryptocurrencies with rising trends and good market cap"""
        rising_cryptos = [name for name, data in self.crypto_db.items() 
                         if data['price_trend'] == 'rising']
        
        if not rising_cryptos:
            return "🤔 No cryptocurrencies are showing strong upward trends right now. Consider waiting for better market conditions!"
        
        # Prioritize high market cap coins among rising ones
        best_crypto = max(rising_cryptos, 
                         key=lambda x: 1 if self.crypto_db[x]['market_cap'] == 'high' else 0)
        
        data = self.crypto_db[best_crypto]
        return f"""🚀 **{best_crypto} ({data['symbol']})** looks promising for profits!
        
📈 Trend: {data['price_trend'].title()} 
💰 Market Cap: {data['market_cap'].title()}
⚠️ Risk Level: {data['risk_level'].title()}
💡 About: {data['description']}

Great momentum for potential gains! 📊"""

    def compare_cryptocurrencies(self, coin1, coin2):
        """Compare two cryptocurrencies"""
        coin1 = coin1.title()
        coin2 = coin2.title()
        
        if coin1 not in self.crypto_db or coin2 not in self.crypto_db:
            available = ", ".join(self.crypto_db.keys())
            return f"❌ Sorry, I can only compare these coins: {available}"
        
        data1 = self.crypto_db[coin1]
        data2 = self.crypto_db[coin2]
        
        comparison = f"""
🆚 **{coin1} vs {coin2}** COMPARISON
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 **{coin1} ({data1['symbol']})**
   └─ Price Trend: {data1['price_trend'].title()}
   └─ Market Cap: {data1['market_cap'].title()}
   └─ Sustainability: {data1['sustainability_score']}/10
   └─ Energy Use: {data1['energy_use'].replace('_', ' ').title()}

📊 **{coin2} ({data2['symbol']})**
   └─ Price Trend: {data2['price_trend'].title()}
   └─ Market Cap: {data2['market_cap'].title()}
   └─ Sustainability: {data2['sustainability_score']}/10
   └─ Energy Use: {data2['energy_use'].replace('_', ' ').title()}

🏆 **Winner for Sustainability**: {coin1 if data1['sustainability_score'] > data2['sustainability_score'] else coin2}
💰 **Better Market Position**: {coin1 if data1['market_cap'] == 'high' and data2['market_cap'] != 'high' else coin2 if data2['market_cap'] == 'high' and data1['market_cap'] != 'high' else 'Tie'}
        """
        return comparison

    def get_coin_info(self, coin_name):
        """Get detailed information about a specific cryptocurrency"""
        coin_name = coin_name.title()
        
        if coin_name not in self.crypto_db:
            available = ", ".join(self.crypto_db.keys())
            return f"❌ I don't have data for {coin_name}. Available coins: {available}"
        
        data = self.crypto_db[coin_name]
        return f"""
📋 **{coin_name} ({data['symbol']}) - DETAILED INFO**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📈 Price Trend: {data['price_trend'].title()}
💰 Market Cap: {data['market_cap'].title()}
🌱 Sustainability Score: {data['sustainability_score']}/10
⚡ Energy Usage: {data['energy_use'].replace('_', ' ').title()}
⚠️ Risk Level: {data['risk_level'].title()}
💡 Description: {data['description']}

{'🌟 Great for eco-investors!' if data['sustainability_score'] >= 7 else '⚡ High energy usage - consider environmental impact' if data['energy_use'] == 'high' else ''}
        """

    def show_all_coins(self):
        """Display all available cryptocurrencies"""
        output = "\n💎 **ALL AVAILABLE CRYPTOCURRENCIES** 💎\n"
        output += "━" * 60 + "\n"
        
        for coin, data in self.crypto_db.items():
            trend_emoji = "🚀" if data['price_trend'] == 'rising' else "📊" if data['price_trend'] == 'stable' else "⚠️"
            eco_emoji = "🌱" if data['sustainability_score'] >= 7 else "⚡"
            
            output += f"{trend_emoji} **{coin} ({data['symbol']})** {eco_emoji}\n"
            output += f"   └─ Trend: {data['price_trend'].title()} | Sustainability: {data['sustainability_score']}/10\n\n"
        
        return output

    def get_personalized_recommendation(self):
        """Provide a balanced recommendation considering both factors"""
        # Calculate a balanced score (profitability + sustainability)
        scored_cryptos = []
        
        for name, data in self.crypto_db.items():
            profit_score = 3 if data['price_trend'] == 'rising' else 2 if data['price_trend'] == 'stable' else 1
            market_score = 2 if data['market_cap'] == 'high' else 1
            sustainability_score = data['sustainability_score']
            
            total_score = (profit_score + market_score + sustainability_score) / 3
            scored_cryptos.append((name, total_score, data))
        
        # Sort by score and get top recommendation
        scored_cryptos.sort(key=lambda x: x[1], reverse=True)
        best_name, best_score, best_data = scored_cryptos[0]
        
        return f"""🎯 **PERSONALIZED RECOMMENDATION FOR {self.user_name.upper()}**

🏆 **{best_name} ({best_data['symbol']})** - Your best balanced choice!

📊 **Overall Score**: {best_score:.1f}/5.0
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📈 Profitability: {best_data['price_trend'].title()} trend
🌱 Sustainability: {best_data['sustainability_score']}/10
💰 Market Position: {best_data['market_cap'].title()} market cap
⚠️ Risk Level: {best_data['risk_level'].title()}

💡 **Why this choice?** {best_data['description']}

🎉 Perfect balance of growth potential and environmental responsibility!
"""

    def process_user_input(self, user_input):
        """Process user input and provide appropriate response"""
        user_input = user_input.lower().strip()
        
        # Exit commands
        if user_input in ['quit', 'exit', 'bye', 'goodbye']:
            return "exit"
        
        # Help command
        if user_input in ['help', '?']:
            self.show_help()
            return "continue"
        
        # Sustainability queries
        if any(word in user_input for word in ['sustainable', 'eco', 'green', 'clean', 'environment']):
            print("Metis:", self.get_sustainable_recommendation())
            return "continue"
        
        # Profitability queries
        if any(word in user_input for word in ['trending', 'rising', 'profitable', 'gains', 'profit']):
            print("Metis:", self.get_profitable_recommendation())
            return "continue"
        
        # Comparison queries
        if 'compare' in user_input:
            words = user_input.split()
            if len(words) >= 3:
                coin1 = words[1] if len(words) > 1 else ""
                coin2 = words[2] if len(words) > 2 else ""
                print("Metis:", self.compare_cryptocurrencies(coin1, coin2))
            else:
                print("Metis: Please specify two coins to compare! Example: 'compare bitcoin ethereum'")
            return "continue"
        
        # Individual coin info
        if 'info' in user_input:
            words = user_input.split()
            if len(words) >= 2:
                coin_name = words[1]
                print("Metis:", self.get_coin_info(coin_name))
            else:
                print("Metis: Which coin would you like info about? Example: 'info bitcoin'")
            return "continue"
        
        # Show all coins
        if any(phrase in user_input for phrase in ['all coins', 'show all', 'list coins', 'available']):
            print("Metis:", self.show_all_coins())
            return "continue"
        
        # General recommendations
        if any(word in user_input for word in ['best', 'recommend', 'suggestion', 'advice']):
            print("Metis:", self.get_personalized_recommendation())
            return "continue"
        
        # Energy usage queries
        if 'energy' in user_input:
            low_energy = [name for name, data in self.crypto_db.items() 
                         if data['energy_use'] in ['low', 'very_low']]
            coins_list = ", ".join(low_energy)
            print(f"Metis: 🌱 Low-energy cryptocurrencies: {coins_list}")
            print("Metis: These are great choices for environmentally conscious investors! 🌍")
            return "continue"
        
        # Market cap queries
        if 'market cap' in user_input:
            high_cap = [name for name, data in self.crypto_db.items() 
                       if data['market_cap'] == 'high']
            coins_list = ", ".join(high_cap)
            print(f"Metis: 💰 High market cap coins (more stable): {coins_list}")
            return "continue"
        
        # Default response for unrecognized input
        responses = [
            f"🤔 I'm not sure about that, {self.user_name}. Try asking about 'sustainable coins', 'trending crypto', or type 'help'!",
            "💭 Hmm, could you rephrase that? I can help with sustainability, profitability, or comparisons!",
            "🔍 I didn't catch that! Ask me about 'eco-friendly coins' or 'profitable investments'!",
            "🤖 Beep boop! Try asking about specific coins or type 'help' to see what I can do!"
        ]
        
        print("Metis:", random.choice(responses))
        return "continue"

    def add_disclaimer(self):
        """Display investment disclaimer"""
        disclaimer = """
⚠️  **IMPORTANT DISCLAIMER** ⚠️
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🚨 This is educational content, NOT financial advice!
💸 Cryptocurrency investments carry HIGH risk
📉 Past performance doesn't guarantee future results  
🧠 Always do your own research before investing
💰 Never invest more than you can afford to lose
🏦 Consider consulting with licensed financial advisors
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        """
        print(disclaimer)

    def run(self):
        """Main chatbot loop"""
        self.display_banner()
        self.greet_user()
        
        print("\n" + "="*50)
        print(f"🗨️  CHAT WITH METIS - Type your questions below!")
        print("="*50 + "\n")
        
        while self.conversation_active:
            try:
                user_input = input(f"{self.user_name}: ").strip()
                
                if not user_input:
                    print("Metis: I'm here when you're ready to chat! 😊")
                    continue
                
                # Add some personality with typing delay
                print("Metis: *thinking...* 🤔")
                time.sleep(1)
                
                result = self.process_user_input(user_input)
                
                if result == "exit":
                    print(f"Metis: Thanks for chatting, {self.user_name}! 🚀")
                    print("Metis: Remember: Invest wisely and stay curious! 💎✨")
                    self.add_disclaimer()
                    self.conversation_active = False
                else:
                    print()  # Add spacing between responses
                    
            except KeyboardInterrupt:
                print(f"\n\nMetis: Goodbye, {self.user_name}! Stay safe in the crypto world! 🌟")
                self.add_disclaimer()
                break
            except Exception as e:
                print(f"Metis: Oops! Something went wrong: {str(e)}")
                print("Metis: Let's try again! 🔄")

def main():
    """Main function to run the chatbot"""
    print("🚀 Initializing Metis...")
    time.sleep(2)
    
    bot = Metis()
    bot.run()

if __name__ == "__main__":
    main()
    