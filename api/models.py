from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(
        max_length=200, default="", null=False, blank=False)
    author = models.CharField(
        max_length=100, default="", null=False, blank=False)
    genre = models.CharField(
        max_length=100, default="", null=False, blank=False)
    price = models.DecimalField(max_digits=4, decimal_places=2, default=00.00)
    summary = models.TextField(default="")
    stars = models.IntegerField(default=0)

    def __str__(self):
        return self.title
