from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.ForeignKey(User, related_name='profiles')
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def sleeping(self):
        try:
            return self.sleep_logs.all()[0].sleeping
        except IndexError:
            return False

class SleepLog(models.Model):
    class Meta:
        ordering = ['-created_at']
        index_together = (
            ('profile', 'created_at')
        )

    profile = models.ForeignKey(Profile, related_name='sleep_logs')
    created_at = models.DateTimeField(auto_now_add=True)
    sleeping = models.BooleanField()
