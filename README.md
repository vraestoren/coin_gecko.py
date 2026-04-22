# <img src="https://www.coingecko.com//favicon-96x96.png" width="40" style="vertical-align:middle;" /> coin_gecko.py
> Web-API for [CoinGecko](https://www.coingecko.com) a platform for fundamental analysis of the crypto market. Tracks price, volume, market capitalisation, exchange data, derivatives, and more.

## Quick Start
```python
from coin_gecko import CoinGecko

coin_gecko = CoinGecko()

# Get global crypto market data
print(coin_gecko.get_global_crypto_data())

# Get Bitcoin price in USD
print(coin_gecko.get_price(coin_ids="bitcoin", vs_currencies="usd"))

# Get top 10 coins by market cap
print(coin_gecko.get_markets(vs_currency="usd", per_page=10))
```

---

## Simple

| Method | Description |
|--------|-------------|
| `get_price(coin_ids, vs_currencies, ...)` | Get current price of one or more coins |
| `get_token_price(platform_id, contract_addresses, vs_currencies, ...)` | Get price by contract address |
| `get_supported_vs_currencies()` | List all supported vs-currencies |

---

## Coins

| Method | Description |
|--------|-------------|
| `get_coins_list(include_platform)` | List all coins with id, name, symbol |
| `get_markets(vs_currency, ...)` | Get coins with market data |
| `get_coin_current_data(coin_id, ...)` | Full data for a single coin |
| `get_coin_tickers(coin_id, ...)` | Tickers for a coin across exchanges |
| `get_coin_historical_data(coin_id, date, ...)` | Historical snapshot by date |
| `get_coin_market_chart(coin_id, vs_currency, days, ...)` | Price/volume chart data |
| `get_coin_market_chart_range(coin_id, vs_currency, from_date, to_date, ...)` | Chart data for a date range |
| `get_coin_ohlc(coin_id, vs_currency, days, ...)` | OHLC candlestick data |

---

## Contract

| Method | Description |
|--------|-------------|
| `get_coin_info_by_contract_address(platform_id, contract_address)` | Coin info via contract address |
| `get_contract_address_market_chart(platform_id, contract_address, vs_currency, days, ...)` | Chart data via contract |
| `get_contract_address_market_chart_range(platform_id, contract_address, vs_currency, from_date, to_date, ...)` | Ranged chart via contract |

---

## Asset Platforms

| Method | Description |
|--------|-------------|
| `get_asset_platforms(filter)` | List all asset platforms (e.g. Ethereum, Solana) |

---

## Categories

| Method | Description |
|--------|-------------|
| `get_all_categories()` | List all coin categories |
| `get_all_categories_with_market_data(order)` | Categories with market cap and volume |

---

## Exchanges

| Method | Description |
|--------|-------------|
| `get_all_exchanges(per_page, page)` | List exchanges with market data |
| `get_exchanges_list()` | Lightweight list of all exchanges |
| `get_exchange(exchange_id)` | Details for a single exchange |
| `get_exchange_tickers(exchange_id, ...)` | Tickers listed on an exchange |
| `get_volume_chart_data(exchange_id, days)` | Exchange volume chart |

---

## Indexes

| Method | Description |
|--------|-------------|
| `get_all_market_indexes(per_page, page)` | List all market indexes |
| `get_market_index(market_id, index_id)` | Single market index |
| `get_indexes_list()` | Lightweight index list |

---

## Derivatives

| Method | Description |
|--------|-------------|
| `get_all_derivative_tickers(include_tickers)` | All derivative tickers |
| `get_all_derivative_exchanges(order, per_page, page)` | List derivative exchanges |
| `get_derivative_exchange_data(exchange_id, include_tickers)` | Data for a derivative exchange |
| `get_derivative_exchanges_list()` | Lightweight derivative exchange list |

---

## Global

| Method | Description |
|--------|-------------|
| `get_exchange_rates()` | BTC exchange rates |
| `search(query)` | Search coins, exchanges, categories |
| `get_trending_search()` | Trending searches in last 24h |
| `get_global_crypto_data()` | Global crypto market overview |
| `get_global_crypto_defi_data()` | Global DeFi market data |
| `get_public_companies_data(coin_id)` | Public companies holding a coin |
