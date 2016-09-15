from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class Details(models.Model):
	price     = models.DecimalField( max_digits=15, decimal_places=2 )
	downPay   = models.DecimalField( max_digits=15, decimal_places=2 )
	intRate   = models.DecimalField( max_digits=15, decimal_places=2 )
	mortTerm  = models.IntegerField()
	taxes     = models.DecimalField( max_digits=15, decimal_places=2 )
	insurance = models.DecimalField( max_digits=15, decimal_places=2 )

class House(models.Model):
	address      = models.CharField(max_length=200)
	city         = models.CharField(max_length=200)
	state        = models.CharField(max_length=50)
	zip		     = models.IntegerField()
	details      = models.ForeignKey( Details )
	created_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		details = '{}, {}, {}, {}'.format( self.address, self.city, self.state, self.zip )
		return details