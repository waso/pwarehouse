from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name

class Storage(models.Model):
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name

class Currency(models.Model):
    name = models.CharField(max_length=3)
    def __unicode__(self):
        return self.name

#class Price(models.Model):
#    amount = models.DecimalField(max_digits=11, decimal_places=5)
#    currency = models.ForeignKey(Currency)
#    def __unicode__(self):
#        return str(self.amount), ' ', self.currency

class TaxRate(models.Model):
    percentage = models.IntegerField(max_length=2)
    def __unicode__(self):
        return str(self.percentage)

class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category)
    tax_rate = models.ForeignKey(TaxRate)
    def __unicode__(self):
        return self.name
        
class ItemsBucket(models.Model):
    item = models.ForeignKey(Item)
    count = models.IntegerField(max_length=6)
    buy_price = models.DecimalField(max_digits=11, decimal_places=5)
    sell_price = models.DecimalField(max_digits=11, decimal_places=5)
    tax = models.ForeignKey(TaxRate)
