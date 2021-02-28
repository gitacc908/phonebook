from django.db import models

# Create your models here.
class PhoneBook(models.Model):
	name = models.CharField(max_length=99, verbose_name='name')
	phone = models.CharField(max_length=99, verbose_name='phone')
	email = models.EmailField(max_length=99, verbose_name='email')


	def __str__(self):
		return self.name