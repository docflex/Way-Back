from django.db import models

class YouTubeVideo(models.Model):
    # Fields to store information about a YouTube video
    
    kind = models.CharField(max_length=50)  # The type of resource ("youtube#searchResult")
    etag = models.CharField(max_length=50)  # Entity tag for the video data
    video_id = models.CharField(max_length=50, unique=True)  # Unique identifier for the video
    published_at = models.DateTimeField()  # Date and time when the video was published
    channel_id = models.CharField(max_length=50)  # ID of the video's channel
    title = models.CharField(max_length=200)  # Title of the video
    description = models.TextField()  # Description of the video
    default_thumbnail_url = models.URLField()  # URL of the default thumbnail
    medium_thumbnail_url = models.URLField()  # URL of the medium-sized thumbnail
    high_thumbnail_url = models.URLField()  # URL of the high-resolution thumbnail
    channel_title = models.CharField(max_length=100)  # Title of the video's channel
    live_broadcast_content = models.CharField(max_length=20)  # Live broadcast status of the video
    publish_time = models.DateTimeField()  # Time when the video was published (formatted)

    def __str__(self):
        # Human-readable representation of the object
        return f'Video ID: {self.video_id}'
