from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    body = models.TextField()
    author = models.ForeignKey('Author', on_delete=models.PROTECT, related_name='articles')

    def __str__(self):
        return self.title
