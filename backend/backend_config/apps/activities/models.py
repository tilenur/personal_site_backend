from django.db import models


# Create your models here.
class Activity(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()
    image = models.ImageField(upload_to="activities/")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Activity"
        verbose_name_plural = "Activities"
