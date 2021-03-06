from django.db import models

# Create your models here.
class Query(models.Model):
    account = models.CharField(max_length=80)
    query_time = models.DateField()
    meta_data = models.CharField(max_length=200)
    bank = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    currency = models.CharField(max_length=20)
    type = models.CharField(max_length=20)

    def __str__(self):
        return self.bank + ": " + self.account