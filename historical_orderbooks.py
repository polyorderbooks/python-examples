import os
from datetime import datetime, timedelta, timezone

from polyorderbooks import PolyOrderbooksClient

with PolyOrderbooksClient(api_key=os.environ["POLYORDERBOOKS_API_KEY"]) as client:
    slug = client.list_markets(search="bitcoin", limit=1)["data"][0]["slug"]
    end = datetime.now(timezone.utc)
    start = end - timedelta(hours=6)
    ts = lambda dt: dt.strftime("%Y-%m-%dT%H:%M:%SZ")
    books = client.get_market_books(
        slug,
        start_ts=ts(start),
        end_ts=ts(end),
        resolution="60s",
        limit=10,
    )
    for outcome, points in books["data"].items():
        for point in points[:3]:
            bids, asks = point.get("bids") or [], point.get("asks") or []
            print(
                point["t"],
                outcome,
                "bid",
                bids[0][0] if bids else None,
                "ask",
                asks[0][0] if asks else None,
            )
