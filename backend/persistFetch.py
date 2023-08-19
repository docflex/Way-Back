import time
import requests
import sys

i = 1
while i < 10:
    url = 'http://127.0.0.1:8000/videos/'  # Change the URL to your actual API endpoint
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print('Fetched YouTube videos:', response.status_code)
        else:
            print('Unexpected response status code:', response.status_code)
            sys.exit(1)  # Exit with non-zero status code
    except requests.exceptions.RequestException as e:
        print('Error:', e)
        sys.exit(1)  # Exit with non-zero status code
    
    time.sleep(10)  # Wait for 10 seconds
    i += 1
