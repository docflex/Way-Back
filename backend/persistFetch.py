import time
import requests

i = 1
while i < 10:
    url = 'http://127.0.0.1:8000/videos/'  # Change the URL to your actual API endpoint
    response = requests.get(url)
    print('Fetched YouTube videos:', response.status_code)
    time.sleep(10)  # Wait for 10 seconds
    i += 1