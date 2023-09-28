from django.apps import AppConfig
import redis


class NewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news'


red = redis.Redis(
    host='redis-10946.c284.us-east1-2.gce.cloud.redislabs.com',
    port=10946,
    password='ttSVozCYqxUDd2qNBLxFFHK0CYOedYHS'

)
