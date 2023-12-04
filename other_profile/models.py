from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Report(models.Model):
    reported_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='reported_user')
    reason = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Report #{self.id} -> {self.reported_user.username}'
