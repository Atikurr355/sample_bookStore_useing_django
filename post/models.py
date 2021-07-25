from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to="blogs_image/")
    slug = models.SlugField(max_length=100)
    time = models.TimeField(auto_now_add=True)


    def __str__(self):
        return self.title