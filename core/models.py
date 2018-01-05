from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Meetup(models.Model):
    name = models.CharField(max_length = 200)
    created = models.DateTimeField(auto_now_add = True)
    created_by = models.ForeignKey(User, related_name = 'created_meetups', on_delete = models.CASCADE)
    meetup_image = models.ImageField(upload_to = "%Y/%m/%d/meetup_cover")
