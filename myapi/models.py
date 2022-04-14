from django.db import models


class Stock(models.Model):
	type = models.CharField(max_length=60)
	amount = models.IntegerField()
