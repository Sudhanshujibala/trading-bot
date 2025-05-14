# Binance Futures Testnet Trading Bot  

A Python-based trading bot for Binance Futures Testnet that supports **market** and **limit** orders with logging and error handling.  

 Features  
- Place **market** and **limit** orders  
- Input validation for symbols, sides, and quantities  
- Logging to `bot.log` for debugging  
- Works with Binance Futures **Testnet**  




Setup  

### 1. Get Binance Testnet API Keys  
- Register at [Binance Futures Testnet](https://testnet.binancefuture.com)  
- Go to **API Management** and create a new API key  

### 2. Clone the Repository  
bash
git clone https://github.com/yourusername/binance-trading-bot.git
cd binance-trading-bot





Install Dependencies
bash
pip install python-binance python-dotenv

 
 


Add Your API Keys
Create a .env file in the project folder:

bash
touch .env
Add your API keys:

env
API_KEY=your_testnet_api_key_here
API_SECRET=your_testnet_api_secret_here





Run the Bot
bash
python bot.py
Follow the prompts to place orders.

Usage Example
bash
Enter symbol (e.g., BTCUSDT): BTCUSDT  
Enter side (BUY or SELL): BUY  
Enter quantity: 0.01  
Enter order type (MARKET/LIMIT): LIMIT  
Enter price: 50000  
✅ Order placed and logged in bot.log
