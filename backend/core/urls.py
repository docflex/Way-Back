from django.urls import path
from django.contrib import admin
from rest_framework import routers
from youtubeScrapper import views

# Create a DefaultRouter instance
router = routers.DefaultRouter()

# Add your router URLs to the urlpatterns
urlpatterns = router.urls

urlpatterns += [
    path('admin/', admin.site.urls),
    path('videos/', views.YouTubeVideoAPIView.as_view()),  # New endpoint for fetching YouTube videos
]
