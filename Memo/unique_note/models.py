
from django.db import models


class Note(models.Model):
    note = models.CharField(max_length=200)
    pub_date = models.DateField()

    def __str__(self):
        return self.note
