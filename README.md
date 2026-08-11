# PolyOrderbooks Python examples

Runnable scripts for the [PolyOrderbooks API](https://docs.polyorderbooks.com) using the official [Python SDK](https://github.com/polyorderbooks/python-sdk).

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export POLYORDERBOOKS_API_KEY="pob_..."
```

Get an API key at [polyorderbooks.com/signup](https://polyorderbooks.com/signup).

## Examples

| Script | Description |
| --- | --- |
| [`historical_orderbooks.py`](historical_orderbooks.py) | Fetch historical L2 books for one market and print best bid/ask |

```bash
python historical_orderbooks.py
```

Need the concepts behind realistic fill assumptions? Read the [historical Polymarket order book data for backtesting](https://polyorderbooks.com/blog/historical-polymarket-order-book-data-backtesting) guide.

## Guides

For broader context on historical data sources and practical retrieval patterns:

- [Polymarket historical data: prices, trades, order books, and API access](https://polyorderbooks.com/blog/polymarket-historical-data-download-prices-trades-order-books)
- [Historical Polymarket order book data for backtesting](https://polyorderbooks.com/blog/historical-polymarket-order-book-data-backtesting)
- [Polymarket price history with Python](https://polyorderbooks.com/blog/polymarket-price-history-download-python)
