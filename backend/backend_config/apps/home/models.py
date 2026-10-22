from django.db import models


# Create your models here.
class Home(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="home/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Home"
        verbose_name_plural = "Home"
