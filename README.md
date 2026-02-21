# Distributed Calculator

A simple client-server calculator using **ZeroMQ (ZMQ)** to demonstrate parallel and distributed computing with real-time JSON requests.

---

## Features
- Handles basic math operations: add, subtract, multiply, divide
- Returns errors for invalid input
- Demonstrates REQ/REP messaging pattern in ZeroMQ

---

## Installation

1. Clone the repository:
git clone https://github.com/YOUR_USERNAME/Distributed-Calculator.git
cd parallel

2. Install dependencies:
pip install -r requirements.txt

---

## Usage

1. Run the server:
python rq_server.py

2. Run the client:
python rq_client.py

3. Example request:
{"a": 10, "b": 5, "op": "add"}

4. Example response:
{"result": 15}

---

## License

MIT License

