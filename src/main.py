import os
from dotenv import load_dotenv
import sseclient

# load environment variables from .env file
load_dotenv()

SSE_SUBSCRIPTION_URL = os.getenv('SSE_SUBSCRIPTION_URL')
messages = sseclient.SSEClient(SSE_SUBSCRIPTION_URL)

for msg in messages:
    print(msg)