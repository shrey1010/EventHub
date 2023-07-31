from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Event(models.Model):
    EVENT_TYPE_CHOICES = (
        ('Global', 'Global'),
        ('User Specific', 'User Specific'),
    )

    event_name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='event_images/')
    event_type = models.CharField(max_length=20, choices=EVENT_TYPE_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    registered_users = models.ManyToManyField(
        User, related_name='registered_events', blank=True)
    tags = models.ManyToManyField(Tag)
    
    def __str__(self):
        return self.event_name

    def like_event(self, user):
        Like.objects.get_or_create(event=self, user=user)

    def unlike_event(self, user):
        Like.objects.filter(event=self, user=user).delete()

    def is_liked_by_user(self, user):
        return Like.objects.filter(event=self, user=user).exists()

    def update_event(self, **kwargs):
        for field, value in kwargs.items():
            setattr(self, field, value)
        self.save()


class Like(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('event', 'user')
