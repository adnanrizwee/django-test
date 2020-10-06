from django.db import models

# Create your models here.
class Test(models.Model):
	testData = models.CharField(max_length=100)
	def __str__(self):
		return self.testData