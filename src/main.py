import sseclient

messages = sseclient.SSEClient('http://localhost:5000/sse-subscribe')

for msg in messages:
    print(msg)