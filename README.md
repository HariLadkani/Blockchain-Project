# Simple Blockchain Implementation with Flask

This project is a simple blockchain implementation using Python and Flask. It provides basic blockchain functionalities such as creating new transactions, mining blocks, and retrieving the current blockchain state via a RESTful API.


## Introduction

A blockchain is a distributed ledger used to store transactions securely. This project demonstrates a minimalistic blockchain implementation where users can:
- Add transactions to the blockchain.
- Mine new blocks by solving proof-of-work challenges.
- Retrieve the blockchain state.

---

## Features

- **Add Transactions**: Add sender, recipient, and transaction amount to the blockchain.
- **Mine Blocks**: Generate proof-of-work and append new blocks to the chain.
- **View Blockchain**: Retrieve the current state of the blockchain.

---

## Tech Stack

- **Backend**: Flask (Python)
- **Core Blockchain**: Python (custom implementation)
- **UUID**: To generate unique identifiers for nodes
- **Hashing**: SHA-256 (via `hashlib`)

