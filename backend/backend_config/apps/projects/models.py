from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    live_url = models.URLField(blank=True, null=True)
    preview = models.ImageField(upload_to="projects/", blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
