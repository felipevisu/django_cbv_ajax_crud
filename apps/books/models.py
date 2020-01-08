from django.db import models

class Book(models.Model):
    HARDCOVER = 1
    PAPERBACK = 2
    EBOOK = 3

    BOOK_TYPES = (
        (HARDCOVER, 'Hardcover'),
        (PAPERBACK, 'Paperback'),
        (EBOOK, 'E-book'),
    )

    title = models.CharField(max_length=50)
    author = models.CharField(max_length=30, blank=True)
    pages = models.IntegerField(blank=True, null=True)
    book_type = models.PositiveSmallIntegerField(choices=BOOK_TYPES)
