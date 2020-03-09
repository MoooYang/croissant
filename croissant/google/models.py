from django.db import models

class Query(models.Model):
    query_text = models.CharField(max_length=200)
    search_data = models.DateField()

    def __str__(self):
        return self.query_text
