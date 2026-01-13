print("S")

# Project 15: Astrology + Market Sentiment + Order Book Confirmation Tool

import requests
import pandas as pd

def get_binance_order_book(symbol="BTCUSDT", limit=10):
    url = f"https://api.binance.com/api/v3/depth?symbol={symbol}&limit={limit}"
    response = requests.get(url)
    data = response.json()
    
    bids = pd.DataFrame(data['bids'], columns=['Price', 'Quantity'], dtype=float)
    asks = pd.DataFrame(data['asks'], columns=['Price', 'Quantity'], dtype=float)
    
    return bids, asks

def get_binance_volume(symbol="BTCUSDT"): 
    url = f"https://api.binance.com/api/v3/ticker/24hr?symbol={symbol}"
    response = requests.get(url)
    data = response.json()
    return float(data['quoteVolume']), float(data['priceChangePercent'])

def make_decision(astrology_signal, bids, asks, volume, price_change):
    total_bid_qty = bids['Quantity'].sum()
    total_ask_qty = asks['Quantity'].sum()

    print("--- Market Snapshot ---")
    print(f"Total Buy Quantity: {total_bid_qty}")
    print(f"Total Sell Quantity: {total_ask_qty}")
    print(f"24h Volume (USDT): {volume}")
    print(f"24h Price Change (%): {price_change}")

    if astrology_signal == "bullish":
        if total_bid_qty > total_ask_qty and volume > 100000000 and price_change > 0:
            return "📈 CONFIRM: Go LONG (Buy)"
        else:
            return "⏸️ WAIT - Astrology is positive, but market is not supporting."
    elif astrology_signal == "bearish":
        if total_ask_qty > total_bid_qty and volume > 100000000 and price_change < 0:
            return "📉 CONFIRM: Go SHORT (Sell)"
        else:
            return "⏸️ WAIT - Astrology is negative, but market is not confirming."
    else:
        return "❓ Invalid astrology signal. Use 'bullish' or 'bearish'."

# Example Usage:
bids, asks = get_binance_order_book()
volume, price_change = get_binance_volume()
astrology_signal = input("Enter astrology prediction (bullish/bearish): ").lower()
decision = make_decision(astrology_signal, bids, asks, volume, price_change)
print("\n🚦 Final Decision:", decision)
