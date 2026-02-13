"""
Bitcoin Fee Estimator (Python)
Estimates the recommended fee (satoshis per byte) based on mempool size.

Author: Your Name
"""

import requests

def get_mempool_size():
    """Fetch mempool size from mempool.space public API"""
    try:
        response = requests.get("https://mempool.space/api/mempool")
        data = response.json()
        return data["count"]
    except Exception as e:
        print("Error fetching mempool data:", e)
        return None

def estimate_fee(tx_size_bytes=250):
    """Estimate fee in satoshis based on mempool congestion"""
    mempool_count = get_mempool_size()
    if mempool_count is None:
        return None

    # simple formula: base fee + congestion multiplier
    base_fee = 10  # sat/byte
    congestion_fee = mempool_count // 1000
    fee_rate = base_fee + congestion_fee
    return fee_rate * tx_size_bytes

if __name__ == "__main__":
    tx_size = int(input("Enter your transaction size in bytes (default 250): ") or 250)
    fee = estimate_fee(tx_size)
    if fee:
        print(f"Recommended fee: {fee} satoshis (~{fee/100_000_000} BTC)")
    else:
        print("Could not estimate fee.")
