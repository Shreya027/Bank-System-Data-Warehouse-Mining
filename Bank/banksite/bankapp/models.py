
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Csv(models.Model):
    csv = models.FileField(null=False,blank=False)

class Account(models.Model):
    acct_id = models.IntegerField()
    acct_type = models.CharField(max_length=30)
    balance = models.IntegerField(default=-1)
    overdraft_history = models.IntegerField()


class Credit(models.Model):
    timestamp = models.CharField(max_length=100)
    existing_npa = models.DecimalField(decimal_places=2,max_digits=5,default=0)
    cash_reserve= models.DecimalField(decimal_places=2,max_digits=5,default=0)


class Customer(models.Model):
    cust_id = models.IntegerField()
    name = models.CharField(max_length=100)
    birth_date = models.CharField(max_length=20)
    fam_dependency = models.IntegerField()
    account_no = models.IntegerField()
    income = models.IntegerField()
    pincode = models.IntegerField()
    age = models.IntegerField(default=-1)
    first_name = models.CharField(default='UNK',max_length=20)
    last_name= models.CharField(default='UNK', max_length=20)
    def __str__(self):
        return self.name

class Interest(models.Model):
    timestamp = models.CharField(max_length=100)
    mclr = models.DecimalField(decimal_places=2,max_digits=5,default=0)
    fdr = models.DecimalField(decimal_places=2,max_digits=5,default=0)
    def __str__(self):
        return self.timestamp

class Region(models.Model):
    pincode = models.IntegerField()
    address = models.CharField(max_length=200)
