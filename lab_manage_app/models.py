from django.db import models


# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=50, default="")
    last_name = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=50, primary_key=True, unique=True, default="")
    password = models.CharField(max_length=50, default="")
    phone_number = models.CharField(max_length=50, default="")
    is_admin = models.BooleanField()

    class Meta:
        db_table = "users"


# TODO: Add value validations
class Books(models.Model):
    book_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, default="")
    total_pages = models.CharField(max_length=100, default="")
    rating = models.CharField(max_length=100, default="")
    isbn = models.CharField(max_length=100, default="")
    author_name = models.CharField(max_length=100, default="")
    publication = models.CharField(max_length=100, default="")
    price = models.CharField(max_length=100, default="")

    class Meta:
        db_table = "books"
