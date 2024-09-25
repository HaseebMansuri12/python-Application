from django.db import models

# Create your models here.
class taskModel(models.Model):
	name=models.CharField(max_length=20)
	venue=models.CharField(max_length=30)

def __str__(self):
	return self.name;

class userModel(models.Model):
	uname=models.CharField(max_length=20)
	city=models.CharField(max_length=30)
	psw=models.CharField(max_length=20)

def __str__(self):
	return self.name;