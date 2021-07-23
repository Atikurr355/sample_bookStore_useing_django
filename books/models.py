from django.db import models

# Create your models here.
class Book(models.Model):
    book_title = models.CharField(max_length=150)
    book_details = models.CharField(max_length=300)
    book_author = models.CharField(max_length=100)
    book_image = models.ImageField(upload_to="book_images/")
    book_path = models.FileField(upload_to='book_path/')


    def __str__(self):
        return self.book_title
        return self.book_details
        return self.book_author
    