from django.db import models

class Mahmud(models.Model):
	name = models.CharField(max_length=100)
	roll = models.IntegerField() #ForeignKey('auth.user',on_delete=models.CASCADE,)


	def __str__(self):
		return self.name

class Hossain(models.Model):
	name = models.CharField(max_length=100)
	roll = models.IntegerField() #ForeignKey('auth.user',on_delete=models.CASCADE,)


	def __str__(self):
		return self.name


class Lamyaa(models.Model):
	name = models.CharField(max_length=100)
	roll = models.IntegerField() #ForeignKey('auth.user',on_delete=models.CASCADE,)


	def __str__(self):
		return self.name


class Nowsin(models.Model):
	name = models.CharField(max_length=100)
	roll = models.IntegerField() #ForeignKey('auth.user',on_delete=models.CASCADE,)


	def __str__(self):
		return self.name
