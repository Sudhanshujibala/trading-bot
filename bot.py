import os
from binance.client import Client
from dotenv import load_dotenv
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('bot.log'),
        logging.StreamHandler()
    ]
)

load_dotenv()  # Load .env variables

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret)
        self.client.API_URL = 'https://testnet.binancefuture.com'
    
    @staticmethod
    def validate_input(symbol, side, quantity):
        if not symbol.isalpha():
            raise ValueError("Symbol must be alphabetic (e.g. BTCUSDT)")
        if side not in ['BUY', 'SELL']:
            raise ValueError("Side must be BUY or SELL")
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
    
    def place_limit_order(self, symbol, side, quantity, price):
        try:
            self.validate_input(symbol, side, quantity)
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type='LIMIT',
                timeInForce='GTC',
                quantity=quantity,
                price=price
            )
            logging.info(f"Limit order placed: {order}")
            return order
        except Exception as e:
            logging.error(f"Limit order failed: {e}")
            raise

    def place_market_order(self, symbol, side, quantity):
        try:
            self.validate_input(symbol, side, quantity)
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type='MARKET',
                quantity=quantity
            )
            logging.info("✅ Market Order Placed:")
            logging.info(order)
            return order
        except Exception as e:
            logging.error(f"❌ Error placing order: {str(e)}")
            raise

if __name__ == "__main__":
    bot = BasicBot(API_KEY, API_SECRET)
    
    print("\nBinance Futures Trading Bot")
    print("--------------------------")
    
    symbol = input("Enter symbol (e.g., BTCUSDT): ").upper()
    side = input("Enter side (BUY or SELL): ").upper()
    quantity = float(input("Enter quantity: "))
    
    order_type = input("Enter order type (MARKET/LIMIT): ").upper()
    
    if order_type == "LIMIT":
        price = float(input("Enter price: "))
        bot.place_limit_order(symbol, side, quantity, price)
    else:
        bot.place_market_order(symbol, side, quantity)