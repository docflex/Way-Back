from rest_framework import serializers
from .models import YouTubeVideo

class YouTubeVideoSerializer(serializers.ModelSerializer):
    # Serializer for converting YouTubeVideo model instances into JSON format
    
    class Meta:
        model = YouTubeVideo
        fields = (
            'kind',  # Type of resource
            'etag',  # Entity tag for the video data
            'video_id',  # Unique identifier for the video
            'published_at',  # Date and time of video publication
            'channel_id',  # ID of the video's channel
            'title',  # Title of the video
            'description',  # Description of the video
            'default_thumbnail_url',  # URL of default thumbnail
            'medium_thumbnail_url',  # URL of medium-sized thumbnail
            'high_thumbnail_url',  # URL of high-resolution thumbnail
            'channel_title',  # Title of the video's channel
            'live_broadcast_content',  # Live broadcast status of the video
            'publish_time'  # Time when the video was published (formatted)
        )
