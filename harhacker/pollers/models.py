from django.db import models
from django.contrib.auth import models as user_models

class Har(models.Model):
    user = models.ForeignKey(user_models.User)
    url = models.CharField(max_length=1024, blank=False)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
