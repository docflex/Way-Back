import time
import requests
import sys

# Initialize a set to keep track of fetched video IDs
fetched_video_ids = set()

def print_response(response):
    print("Here are the Newly Fetched Videos:\n")
    data = response.json()["data"]
    items = data["items"]
    for item in items:
        video_id = item["video_id"]
        if video_id not in fetched_video_ids:
            fetched_video_ids.add(video_id)
            print("Video ID:", video_id)
            print("Title:", item["title"])
            print("Published Time:", item["published_at"])
            print("\n")

while True:
    url = 'http://127.0.0.1:8000/videos/'  # Change the URL to your actual API endpoint
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print('Successfully Fetched YouTube videos:', response.status_code)
            print_response(response)  # Print new video data
        else:
            print('Unexpected response status code:', response.status_code)
            sys.exit(1)  # Exit with non-zero status code
    except requests.exceptions.RequestException as e:
        print('Error:', e)
        sys.exit(1)  # Exit with non-zero status code
    
    time.sleep(10)  # Wait for 10 seconds
