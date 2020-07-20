from django.db import models


class Book(models.Model):
    class Meta:
        db_table = "book"
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    title = models.CharField(max_length=100)
    author_name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
