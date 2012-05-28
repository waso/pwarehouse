from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from models import MmDocument, MmDocumentEntry, ItemsBucket, Storage, Currency, DocumentType
from forms import MMForm, MMItem
from datetime import datetime

def mm(request):
	# show list of all invoices
	docs = MmDocument.objects.all()
	return render_to_response('storage/mm.html', 
		{'mm_active':'active',
		'docs': docs}, 
		context_instance = RequestContext(request))

def view(request, doc_id):
	try:
		doc = MmDocument.objects.get(pk = doc_id)
	except MmDocument.DoesNotExist:
		return redirect ('/documents/mm')
	doc_items = MmDocumentEntry.objects.filter(document = doc)

	return render_to_response('storage/mm.html', 
		{'mm_active':'active',
		'doc_items': doc_items,
		'doc': doc}, 
		context_instance = RequestContext(request))
	pass

def add(request):
	if request.method == 'POST':
		pass
		mm_items = []
		errors = []
		form = MMForm(request.POST)
		from_storage = None
		to_storage = None

		# validate submitted items and prepare MM draft in user's session
		for k,v in request.POST.iteritems():
			if k.startswith('item_id_'):
				try:
					iid = k.replace('item_id_', '')
					pkey = int(v)
					bit = ItemsBucket.objects.get(pk = pkey)

					t = MMItem()
					t.ordinal = iid
					t.id = str(pkey)
					t.count = str(int(request.POST.get('item_amount_' + iid)))
					t.name = bit.item.name
					mm_items.append(t)
				except DoesNotExist:
					errors.append('Incorrect item id ' + pkey)

		mm_items.sort(key=lambda MMItem: MMItem.ordinal, reverse=False)

		for item in mm_items:
			db_item = ItemsBucket.objects.get(pk = item.id)
			if int(item.count) > int(db_item.count):
				errors.append('To many items of ' + db_item.item.name)

		if "from_storage_id" in request.POST and request.POST["from_storage_id"]:
			try:
				from_storage = Storage.objects.get(pk = request.POST.get('from_storage_id'))
			except DoesNotExist:
				errors.append('Incorrect from storage id')

		if "to_storage_id" in request.POST and request.POST["to_storage_id"]:
			try:
				to_storage = Storage.objects.get(pk = request.POST.get('to_storage_id'))
			except DoesNotExist:
				errors.append('Incorrect to storage id')

		if not errors and form.is_valid():
			mmplus = DocumentType.objects.get(name='mmplus')
			mmminus = DocumentType.objects.get(name='mmminus')
			from_storage = Storage.objects.get(pk = form.cleaned_data['from_storage_id'])
			to_storage = Storage.objects.get(pk = form.cleaned_data['to_storage_id'])

			doc_p = MmDocument()
			doc_p.doc_type = mmplus
			doc_p.number = form.cleaned_data['doc_number']
			doc_p.storage = to_storage
			doc_p.date = datetime.now()
			doc_p.save()

			doc_m = MmDocument()
			doc_m.date = datetime.now()
			doc_m.doc_type = mmminus
			doc_m.number = form.cleaned_data['doc_number']
			doc_m.storage = from_storage
			doc_m.date = datetime.now()
			doc_m.save()

			for item in mm_items:
				source_bucket = ItemsBucket.objects.get(pk = item.id)
				p_entry = MmDocumentEntry(
					document = doc_p, 
					item = source_bucket.item, 
					count = int(item.count))
				p_entry.save()
				m_entry = MmDocumentEntry(
					document = doc_m, 
					item = source_bucket.item, 
					count = -int(item.count))
				m_entry.save()

				dest_bucket = ItemsBucket.objects \
					.filter(item = source_bucket.item) \
					.filter(buy_price = source_bucket.buy_price) \
					.filter(sell_price = source_bucket.sell_price) \
					.filter(storage = to_storage)

				r = list(dest_bucket[:1])
				if r:
					print 'found ' + str(dest_bucket.count()) + ' matching destination buckets'
					dest_bucket = r[0]
					dest_bucket.count = dest_bucket.count + int(item.count)
				else:
					print 'creating new destination bucket'
					dest_bucket = ItemsBucket(
						item = source_bucket.item, 
						count = item.count, 
						buy_price = source_bucket.buy_price, 
						sell_price = source_bucket.sell_price, 
						storage = to_storage)
				source_bucket.count = source_bucket.count - int(item.count)
				source_bucket.save()
				dest_bucket.save()
			return redirect ('/documents/mm')
		else:
			# errors occured, redisplay the form with errors
			print errors
			items = ItemsBucket.objects.filter(count__gt=0)
			storages = Storage.objects.all()
			currencies = Currency.objects.all()
			return render_to_response('storage/mm_add.html', 
					{'mm_active':'active', 
					'from_storage': from_storage,
					'to_storage': to_storage,
					'items': items,
					'form' : form,
					'mm_items': mm_items,
					'storages': storages,
					'currency': currencies[0]},
					context_instance = RequestContext(request))
	else:
		items = ItemsBucket.objects.filter(count__gt=0)
		storages = Storage.objects.all()
		currencies = Currency.objects.all()
		return render_to_response('storage/mm_add.html', 
			{'mm_active':'active',
			'items': items,
			'storages': storages,
			'currency': currencies[0]},
			context_instance = RequestContext(request))