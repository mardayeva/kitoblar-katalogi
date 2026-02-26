from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=150, blank=True)
    year = models.PositiveIntegerField(null=True, blank=True)
    genre = models.CharField(max_length=80, blank=True)

    short_desc = models.TextField(help_text="Katalog kartochkasida ko‘rinadi")
    full_desc = models.TextField(help_text="Sharh sahifasida batafsil chiqadi")

    slug = models.SlugField(unique=True)
    pdf_file = models.FileField(upload_to="books/pdfs/", null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title