from django.db import models

class Category(models.Model):
    name = models.CharField(max_length = 200)
    def __unicode__(self):
        return self.name

class Storage(models.Model):
    name = models.CharField(max_length = 200)
    def __unicode__(self):
        return self.name

class Currency(models.Model):
    name = models.CharField(max_length = 3)
    def __unicode__(self):
        return self.name

class Price(models.Model):
    amount = models.DecimalField(max_digits = 11, decimal_places = 5)
    currency = models.ForeignKey(Currency)
    def __unicode__(self):
        return str(self.amount) + ' ' + self.currency.name

class TaxRate(models.Model):
    percentage = models.IntegerField(max_length = 2)
    def __unicode__(self):
        return str(self.percentage)

class Item(models.Model):
    name = models.CharField(max_length = 200)
    description = models.TextField()
    category = models.ForeignKey(Category)
    tax_rate = models.ForeignKey(TaxRate)
    def __unicode__(self):
        return self.name
        
class ItemsBucket(models.Model):
    item = models.ForeignKey(Item)
    count = models.IntegerField(max_length = 6)
    buy_price = models.ForeignKey(Price, related_name = 'buy_prices')
    sell_price = models.ForeignKey(Price, related_name = 'sell_prices')
    storage = models.ForeignKey(Storage)
    def __unicode__(self):
        return self.item.name + ' in ' + storage.name + ' (' + count + ')'

class Country(models.Model):
    name = models.CharField(max_length = 30)
    def __unicode__(self):
        return self.name

class Client(models.Model):
    name = models.CharField(max_length = 255)
    address = models.CharField(max_length = 255)
    zip_code = models.CharField(max_length = 6)
    country = models.ForeignKey(Country)
    def __unicode__(self):
        return self.name

class DocumentType(models.Model):
    name = models.CharField(max_length = 30, unique=True)

class DocumentEntry(models.Model):
    item = models.ForeignKey(Item)
    count = models.IntegerField(max_length = 6)
    gross_price = models.ForeignKey(Price)

class Document(models.Model):
    doc_type = models.ForeignKey(DocumentType)
    number = models.CharField(max_length = 30)
    items = models.ManyToManyField(DocumentEntry)
    client = models.ForeignKey(Client)