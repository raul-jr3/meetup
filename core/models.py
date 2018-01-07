from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Meetup(models.Model):
    meetup_name = models.CharField(max_length = 200)
    created = models.DateTimeField(auto_now_add = True)
    created_by = models.ForeignKey(User, related_name = 'created_meetups', on_delete = models.CASCADE)
    meetup_image = models.ImageField(upload_to = "%Y/%m/%d/meetup_cover")
    attendees = models.ForeignKey(User, related_name = "attending", on_delete = models.CASCADE, blank = True, null = True)
    not_sure = models.ForeignKey(User, related_name = "not_sure", on_delete = models.CASCADE, blank = True, null = True)
    description = models.TextField()
    meetup_time = models.DateTimeField()
    meetup_place = models.CharField(max_length = 300)
    active = models.BooleanField(default = True)

    def get_absolute_url(self):
        return reverse('core:meetup_detail', args = [self.id])
