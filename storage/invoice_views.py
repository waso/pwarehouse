from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.forms import ModelForm
from django.http import HttpResponseRedirect
from models import Item, ItemsBucket, Category, Storage, Client, Country, InvoiceDocument, InvoiceDocumentEntry, Currency
from collections import defaultdict
from forms import InvoiceItem, InvoiceForm
from datetime import datetime

def invoice(request):
	# show list of all invoices
	invoices = InvoiceDocument.objects.all()
	return render_to_response('storage/invoice.html', 
		{'invoice_active':'active',
		'invoices': invoices}, 
		context_instance = RequestContext(request))

def invoice_add(request):
	if request.method == 'POST':
		invoice_items = []
		errors = []
		form = InvoiceForm(request.POST)
		client = ""

		# validate submitted items and prepare invoice draft in user's session
		for k,v in request.POST.iteritems():
			if k.startswith('item_id_'):
				try:
					iid = k.replace('item_id_', '')
					pkey = int(v)
					bit = ItemsBucket.objects.get(pk = pkey)

					t = InvoiceItem()
					t.ordinal = iid
					t.id = str(pkey)
					t.count = str(int(request.POST.get('item_amount_' + iid)))
					t.name = bit.item.name
					t.sell_price = str(bit.sell_price)
					t.tax = str(bit.item.tax_rate)
					invoice_items.append(t)
				except DoesNotExist:
					errors.append('Incorrect item id ' + pkey)

		invoice_items.sort(key=lambda InvoiceItem: InvoiceItem.ordinal, reverse=False)

		for item in invoice_items:
			db_item = ItemsBucket.objects.get(pk = item.id)
			if int(item.count) > int(db_item.count):
				errors.append('To many items of ' + db_item.item.name)

		if "client_id" in request.POST and request.POST["client_id"]:
			try:
				client = Client.objects.get(pk = request.POST.get('client_id'))
			except DoesNotExist:
				errors.append('Incorrect client id')

		if not errors and form.is_valid():
			# no errors, save invoice and push changes
			doc = InvoiceDocument()
			doc.number = form.cleaned_data['invoice_number'] + '/2012'
			doc.date = datetime.now()
			doc.client = client
			doc.save()
			for item in invoice_items:
				db_item = ItemsBucket.objects.get(pk = item.id)
				t = InvoiceDocumentEntry()
				t.item = db_item.item
				t.count = item.count
				price = db_item.sell_price
				tax = db_item.item.tax_rate.percentage
				net_price = float(price - (price / 100) * tax)
				t.net_price = net_price
				t.gross_price = item.sell_price
				t.tax = tax
				db_item.count -= int(item.count)
				db_item.save()
				t.document = doc
				t.save()
			return redirect ('/documents/invoice')
		else:
			# errors occured, redisplay the form with errors
			items = ItemsBucket.objects.all()
			clients = Client.objects.order_by('name')
			currencies = Currency.objects.all()
			return render_to_response('storage/invoice_add.html', 
					{'invoice_active':'active', 
					'clients': clients,
					'client': client,
					'items': items,
					'form' : form,
					'invoice_items': invoice_items,
					'currency': currencies[0]},
					context_instance = RequestContext(request))
	else:
		clients = Client.objects.order_by('name')
		items = ItemsBucket.objects.all()
		form = InvoiceForm(initial={'invoice_number': '','client_id': ''})
		currencies = Currency.objects.all()
		return render_to_response('storage/invoice_add.html', 
			{'invoice_active':'active', 
			'clients': clients,
			'items': items,
			'form' : form,
			'currency': currencies[0]},
			context_instance = RequestContext(request))

def invoice_view(request, invoice_id):
	try:
		doc = InvoiceDocument.objects.get(pk = invoice_id)
	except InvoiceDocument.DoesNotExist:
		return redirect ('/documents/invoice')

	net_prices_summary = defaultdict(float)
	gross_prices_summary = defaultdict(float)
	prices_summary = []
	net_prices = []
	total_price = 0.0
	invoice_items = doc.invoicedocumententry_set.all()

	for item in invoice_items:
		total_price += float(item.gross_price)
		net_prices.append(item.net_price)
		net_prices_summary[item.tax] += float(item.net_price)
		gross_prices_summary[item.tax] += float(item.gross_price)
	
	currencies = Currency.objects.all()
	net_prices_summary = net_prices_summary.items()
	gross_prices_summary = gross_prices_summary.items()

	return render_to_response('storage/invoice_view.html', 
    		{'doc': doc,
    		'invoice_items': invoice_items,
    		'net_prices': net_prices,
    		'total_price': total_price,
    		'net_prices_summary': net_prices_summary,
    		'gross_prices_summary': gross_prices_summary,
    		'currency': currencies[0] },
    		context_instance = RequestContext(request))