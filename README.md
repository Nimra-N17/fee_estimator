# Bitcoin Fee Estimator

A simple Python CLI tool that estimates Bitcoin transaction fees in satoshis based on mempool congestion. This project demonstrates basic Python programming, API usage, and Bitcoin transaction concepts.

## Features

- Fetches live mempool data from mempool.space API
- Estimates recommended fee based on transaction size (bytes)
- CLI interface with optional argument for transaction size
- Single-file, beginner-friendly Python project

## Usage

Run the script:

python fee_estimator.py

You can optionally provide a transaction size as an argument:

python fee_estimator.py 300

## Installation

1. Make sure Python 3 is installed
2. Install the `requests` library:

pip install requests

3. Run the script as shown above

## Why I Built This

This project helps beginners understand Bitcoin transaction fees and mempool behavior. It demonstrates reading from APIs, basic Python functions, CLI usage, and clean code structure.

## Future Improvements

- Add more accurate fee estimation (low/medium/high priority)
- Support SegWit and Taproot transactions
- Save results to CSV for analysis
