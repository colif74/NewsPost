from celery import shared_task
from datetime import datetime, timedelta
from .models import Post
from .signals import send_notifications

@shared_task
def frech_news():
    frech_post = Post.objects.all().apply_async(eta = datetime.now() - timedelta(days=7))
    frech_post
