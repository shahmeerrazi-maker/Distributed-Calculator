
import zmq

ctx = zmq.Context()
sock = ctx.socket(zmq.REQ)
sock.connect("tcp://localhost:5555")

# Use print + input to ensure prompts appear
print("Enter number A:", end=" ", flush=True)
a = input()
print("Enter number B:", end=" ", flush=True)
b = input()
print("Operation (add/subtract/multiply/divide):", end=" ", flush=True)
op = input().lower()

request = {"a": a, "b": b, "op": op}
sock.send_json(request)

reply = sock.recv_json()
print("Server replied:", reply)
