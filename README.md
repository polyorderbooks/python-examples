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
