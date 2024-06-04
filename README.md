# Python Server-Sent Events (SSE) Client

![Python Logo](https://www.python.org/static/img/python-logo.png)

This repository contains a Python client script to connect to a server that serves Server-Sent Events (SSE). The client script (`main.py`) runs continuously, listening for SSE events from the server. All events will be printed in the terminal

## Usage

1. Clone this repository:
```bash
git clone https://github.com/your-username/python-sse-client.git
```

2. Navigate to the project directory:
`cd python-sse-client`

3. Install dependencies:
`pip install -r requirements.txt`

4. Navigate to the source folder
`cd src`

5. Create a `.env` file in the src directory and set the SSE_SUBSCRIPTION_URL variable to the URL of the SSE server:
`SUBSCRIPTION_URL=http://your-sse-server-url`

6. Run the client script:
`python main.py`