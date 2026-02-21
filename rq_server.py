# rq_server.py
import zmq
import json

def compute(a, b, op):
    try:
        if op == "add":
            return a + b
        if op == "subtract":
            return a - b
        if op == "multiply":
            return a * b
        if op == "divide":
            if b == 0:
                return {"error": "division by zero"}
            return a / b
        return {"error": f"unknown operation '{op}'"}
    except Exception as e:
        return {"error": str(e)}

def main():
    ctx = zmq.Context()
    sock = ctx.socket(zmq.REP)
    sock.bind("tcp://*:5555")   # bind on port 5555
    print("REQ/REP server listening on tcp://*:5555")

    try:
        while True:
            # server waits for client request
            msg = sock.recv_json()   # expects JSON object
            # Display the received request
            print("Received request:", msg)

            # Validate fields
            a = msg.get("a")
            b = msg.get("b")
            op = msg.get("op")
            if a is None or b is None or op is None:
                reply = {"error":"missing field 'a', 'b' or 'op'"}
            else:
                # ensure numbers (try convert to float or int)
                try:
                    # allow numbers or numeric strings
                    a_num = float(a) if not isinstance(a, (int, float)) else a
                    b_num = float(b) if not isinstance(b, (int, float)) else b
                    res = compute(a_num, b_num, op)
                    reply = {"result": res} if not isinstance(res, dict) else res
                except ValueError:
                    reply = {"error":"a and b must be numbers"}
            # send the reply as JSON
            sock.send_json(reply)
    except KeyboardInterrupt:
        print("\nServer shutting down.")
    finally:
        sock.close()
        ctx.term()

if __name__ == "__main__":
    main()
