import os
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import YouTubeVideo
from apiclient.discovery import build
from dotenv import load_dotenv

load_dotenv()

class YouTubeVideoAPIView(APIView):
    """
    A simple APIView for fetching and storing YouTube video entries.
    """

    def get_youtube_videos(self):
        # Retrieve YouTube API key from environment variables
        api_key = os.getenv("YOUTUBE_API_KEY")
        if not api_key:
            return []
        
        # Create a YouTube API client
        youtube = build('youtube', 'v3', developerKey=api_key)
        
        # Make a request to search for videos with 'avengers' query
        req = youtube.search().list(q='avengers', part='snippet', type='video')
        res = req.execute()
        videos = res.get('items', [])
        
        # Sort videos by published datetime in descending order
        sorted_videos = sorted(videos, key=lambda video: video['snippet']['publishedAt'], reverse=True)
        return sorted_videos

    def get(self, request):
        # Fetch latest YouTube videos
        youtube_videos = self.get_youtube_videos()

        # Iterate through fetched videos and store if not already present
        for video_data in youtube_videos:
            video_id = video_data['id']['videoId']
            if not YouTubeVideo.objects.filter(video_id=video_id).exists():
                YouTubeVideo.objects.create(
                    kind=video_data['kind'],
                    etag=video_data['etag'],
                    video_id=video_id,
                    published_at=video_data['snippet']['publishedAt'],
                    channel_id=video_data['snippet']['channelId'],
                    title=video_data['snippet']['title'],
                    description=video_data['snippet']['description'],
                    default_thumbnail_url=video_data['snippet']['thumbnails']['default']['url'],
                    medium_thumbnail_url=video_data['snippet']['thumbnails']['medium']['url'],
                    high_thumbnail_url=video_data['snippet']['thumbnails']['high']['url'],
                    channel_title=video_data['snippet']['channelTitle'],
                    live_broadcast_content=video_data['snippet']['liveBroadcastContent'],
                    publish_time=video_data['snippet']['publishTime']
                )

        # Retrieve stored videos from the database, order by publish time
        videos = YouTubeVideo.objects.order_by('-published_at')
        serialized_videos = []

        # Serialize video data for API response
        for video in videos:
            serialized_videos.append({
                'kind': video.kind,
                'etag': video.etag,
                'video_id': video.video_id,
                'published_at': video.published_at,
                'channel_id': video.channel_id,
                'title': video.title,
                'description': video.description,
                'default_thumbnail_url': video.default_thumbnail_url,
                'medium_thumbnail_url': video.medium_thumbnail_url,
                'high_thumbnail_url': video.high_thumbnail_url,
                'channel_title': video.channel_title,
                'live_broadcast_content': video.live_broadcast_content,
                'publish_time': video.publish_time
            })

        return Response({"items": serialized_videos})
