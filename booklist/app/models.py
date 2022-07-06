from django.db import models

# Create your models here.


class Institution(models.Model):
    institution_name = models.CharField(max_length=200)

    def __str__(self):
        return self.institution_name


class Direction(models.Model):
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    direction_name = models.CharField(max_length=200)

    def __str__(self):
        return self.direction_name


class List(models.Model):
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=200)
    book_link = models.CharField(max_length=300, default='')

    def __str__(self):
        return self.book_name
