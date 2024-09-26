from django.db import models

# Create your models here.
class Article(models.Model):
  title = models.CharField(max_length=50, null=False, blank=False)
  content = models.TextField(max_length=1000, null=False, blank=False)
  
  def __str__(self):
    return f"{self.title}"