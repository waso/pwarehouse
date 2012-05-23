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
    buy_price = models.DecimalField(max_digits = 11, decimal_places = 5)
    sell_price = models.DecimalField(max_digits = 11, decimal_places = 5)
    storage = models.ForeignKey(Storage)
    def __unicode__(self):
        return str(self.item) + ' in ' + str(self.storage) + ' (' + str(self.count) + ')'

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
    def __unicode__(self):
        return self.name

class InvoiceDocument(models.Model):
    form_of_payment = models.CharField(max_length = 15)
    number = models.CharField(max_length = 30)
    client = models.ForeignKey(Client)
    date = models.DateTimeField()
    def __unicode__(self):
        return self.number

class InvoiceDocumentEntry(models.Model):
    document = models.ForeignKey(InvoiceDocument)
    item = models.ForeignKey(Item)
    count = models.IntegerField(max_length = 6)
    net_price = models.CharField(max_length = 11)
    gross_price = models.CharField(max_length = 11)
    tax = models.CharField(max_length = 2)

class MmDocument(models.Model):
    doc_type = models.ForeignKey(DocumentType)
    number = models.CharField(max_length = 30)
    storage = models.ForeignKey(Storage)
    date = models.DateTimeField()
    def __unicode__(self):
        return self.number

class MmDocumentEntry(models.Model):
    document = models.ForeignKey(MmDocument)
    item = models.ForeignKey(Item)
    count = models.IntegerField(max_length = 6)