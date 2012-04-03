from storage.models import Category, Storage, Currency, Price, TaxRate, Item, ItemsBucket, Country, Client
from decimal import *

#Populates database with initial data
def load():
	#adding new category
	cat1 = Category(name = 'Opony')
	cat1.save()

	#adding new storage
	stor1 = Storage(name = 'Magazyn 1')
	stor1.save()

	#adding new currency
	cur1 = Currency(name = 'PLN')
	cur1.save()

	#adding new price
	pr1 = Price(amount = Decimal(100.0000), currency = cur1)
	pr1.save()

	pr2 = Price(amount = Decimal(120.0000), currency = cur1)
	pr2.save()

	#adding new tax rate
	tx = TaxRate(percentage = 12)
	tx.save()

	#adding new item
	it1 = Item(name = 'Opony 165/65R15', description = 'Opony...', category = cat1, tax_rate = tx)
	it1.save()
	it2 = Item(name = 'Opony 175/65R15', description = 'Opony...', category = cat1, tax_rate = tx)
	it2.save()
	it3 = Item(name = 'Opony 185/65R15', description = 'Opony...', category = cat1, tax_rate = tx)
	it3.save()
	it4 = Item(name = 'Opony 195/65R15', description = 'Opony...', category = cat1, tax_rate = tx)
	it4.save()
	it5 = Item(name = 'Opony 205/65R15', description = 'Opony...', category = cat1, tax_rate = tx)
	it5.save()
	it6 = Item(name = 'Opony 215/65R15', description = 'Opony...', category = cat1, tax_rate = tx)
	it6.save()

	#adding new items bucket
	ib1 = ItemsBucket(item = it1, count = 10, buy_price = pr1, sell_price = pr2, storage = stor1)
	ib1.save()
	ib2 = ItemsBucket(item = it2, count = 10, buy_price = pr1, sell_price = pr2, storage = stor1)
	ib2.save()
	ib3 = ItemsBucket(item = it3, count = 10, buy_price = pr1, sell_price = pr2, storage = stor1)
	ib3.save()
	ib4 = ItemsBucket(item = it4, count = 10, buy_price = pr1, sell_price = pr2, storage = stor1)
	ib4.save()
	

	pl = Country(name = 'Polska')
	pl.save()

	cl1 = Client(name = 'ACMA', address = 'ul. Krakowska 1/2', zip_code = '30100', country = pl)
	cl1.save()