from django.db import models

# Create your models here.
class Video(models.Model):
	title = models.CharField(max_length=200)
	user = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	style = models.CharField(max_length=200)
	choreographer = models.CharField(max_length=200)
	song_title = models.CharField(max_length=200)
	song_artist = models.CharField(max_length=200)
	video_source = models.CharField(max_length=200)
