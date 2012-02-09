import datetime
from django.db import models


class Author(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	birth_date = models.DateField()
	
	def __unicode__(self):
			return 'Author: %s - %s' % (self.pk, self.first_name)


class Article(models.Model):
	author = models.ForeignKey('Author')
	title = models.CharField(max_length=50)
	body = models.TextField()
	created_at = datetime.date.today()
	label = models.ManyToManyField('Label')

class Comment(models.Model):
	name = models.CharField(max_length=50)
	text = models.TextField()
	created_at = datetime.date.today()


class Label(models.Model):
	name = models.CharField(max_length=50)
	
	def __unicode__(self):
			return 'Label: %s - %s' % (self.pk, self.name)
