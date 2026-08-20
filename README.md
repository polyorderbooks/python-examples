# PolyOrderbooks Python examples

Runnable scripts for the [PolyOrderbooks API](https://docs.polyorderbooks.com) using the official
[Python SDK](https://github.com/polyorderbooks/python-sdk) — historical L2 order books, prices, and
liquidity metrics for Polymarket.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export POLYORDERBOOKS_API_KEY="pob_..."
```

Get a key at [polyorderbooks.com/signup](https://polyorderbooks.com/signup). The free tier covers
7 days of history at `60s` resolution, which is enough to run everything here.

## Examples

| Script | What it shows |
| --- | --- |
| [`historical_orderbooks.py`](historical_orderbooks.py) | Find a market, pull 6 hours of L2 books, print best bid/ask per bucket |

```bash
python historical_orderbooks.py
```

```
2026-08-20T01:51:00Z Yes bid 0.056 ask 0.057
2026-08-20T01:52:00Z Yes bid 0.056 ask 0.057
2026-08-20T01:53:00Z Yes bid 0.056 ask 0.057
2026-08-20T01:51:00Z No bid 0.943 ask 0.944
2026-08-20T01:52:00Z No bid 0.943 ask 0.944
2026-08-20T01:53:00Z No bid 0.943 ask 0.944
```

Note `Yes bid + No ask ≈ 1`. The two outcomes are complementary, which is a useful sanity check on
any pipeline you build against this data.

## The response shape

Each bucket in `data[outcome]` looks like this:

```json
{
  "t": "2026-08-20T01:51:00Z",
  "bids": [[0.056, 12500.0], [0.055, 8000.0]],
  "asks": [[0.057, 9800.0], [0.058, 15000.0]]
}
```

`bids` and `asks` are `[price, size]` pairs, **best first** — highest bid, lowest ask. Prices are
probabilities in `[0, 1]`. Depth varies per bucket, so avoid assuming a fixed number of levels:

```python
bids = point.get("bids") or []
best_bid = bids[0][0] if bids else None
```

## Why full ladders matter

Top-of-book tells you the market was at 0.195. The ladder tells you whether you could actually
trade there. If only 13.6 is resting at the best ask, filling 100 units walks the book and averages
**0.2086 — about 4.3% worse**. Backtests built on midpoints miss this entirely.

```python
def cost_to_buy(point, size):
    """Average fill price walking the ask ladder."""
    filled = cost = 0.0
    for price, available in point.get("asks") or []:
        take = min(available, size - filled)
        cost += take * price
        filled += take
        if filled >= size:
            return cost / filled
    return None  # not fillable at any price on this book
```

## Common mistakes

- **Timestamps must be ISO-8601 or unix seconds.** Passing JavaScript-style milliseconds
  (`Date.now()`) is rejected — divide by 1000 first.
- **Reuse the same `start_ts`, `end_ts`, and `resolution`** when following `next_cursor`.
- **`resolution` is required** on history endpoints. Allowed: `1s`, `60s`, `1m`, `5m`, `10m`,
  `15m`, `1h`, `6h`, `1d` — the finest available depends on your plan.
- **Errors return `{"error", "message"}`**; branch on `error`, show `message`.

## Links

- [Documentation](https://docs.polyorderbooks.com) · [Quickstart](https://docs.polyorderbooks.com/quickstart)
- [Working with L2 order books](https://docs.polyorderbooks.com/historical/order-books)
- [Python SDK](https://github.com/polyorderbooks/python-sdk) · [PyPI](https://pypi.org/project/polyorderbooks/)
- [Free sample dataset](https://huggingface.co/datasets/polyorderbooks/polymarket-btc-5min-historical-l2) on Hugging Face
