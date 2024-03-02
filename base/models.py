from django.db import models
from django.utils.text import slugify


class BookModel(models.Model):
    genre = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=20)
    description = models.TextField()
    file = models.FileField(upload_to ='books')
    slug = models.SlugField(default="", null=False)

    def __str__(self):
        return f"{self.title} | {self.author}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title.replace(' ', '-'))
        super().save(*args, **kwargs)