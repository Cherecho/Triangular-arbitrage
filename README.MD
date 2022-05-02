# Triangular-arbitrage
## What Is Triangular Arbitrage?
Triangular arbitrage is the result of a discrepancy between three foreign currencies that occurs when the currency's exchange rates do not exactly match up. These opportunities are rare and traders who take advantage of them usually have advanced computer equipment and/or programs to automate the process.<br><br>
![Triangular-Arbitrage](https://user-images.githubusercontent.com/48016628/166167936-23ad03bb-2825-4efe-ace6-fc8b403b30e8.png)

## Description of this script
This is a triangular arbitrage bot made entirely in python using the ccxt libraries to handle the binance api, It's an endless loop that scans opportunity for binance and executes the operations if found, multi-threaded and with a simple log that it save in a file.<br>
The base money for this bot is ETH, while the exchange currency is BTC, as a result, there are two types of arbitrage:<br> 

- **Forward**: passing first from **ETH** through the **ALT** to then be changed to **BTC** and back to **ETH**
- **Backward**: passing first from **ETH** through **BTC** to then be changed to the selected **ALT** and back to **ETH**

### Does this make money?
In theory yes, if there is any chance, but due to the fees it will be very difficult and I would even dare to say impossible to make any operation since the bot takes into account the binance fee. 


## Dependencies
- ccxt
## Requirements
- [Binance account](https://www.binance.com/es)
## TODO
- Implement something that can alert you remotely like a Telegram Bot
- Make the base currency eligible  
- Add more exchanges
- Make base currency selectable

## Disclaimer:
### This bot is intended to be a Proof-of-concept. The developer will not be responsible for Any losses that are made are as a result of using this tool. Understand the risks involved and Only invest amounts you are willing to lose.