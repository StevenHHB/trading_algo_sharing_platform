from django.db import models
from django.conf import settings


class TradingAlgorithm(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    code = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
