from django.template import RequestContext
from django.shortcuts import render_to_response
from django.forms import ModelForm
from django.http import HttpResponseRedirect
from django.db.models import Q
from models import Item, ItemsBucket, Category, Storage, Client, Country, Document, DocumentType, DocumentEntry
from model_forms import ClientAddForm

def index(request):
    return render_to_response('storage/index.html', {}, context_instance = RequestContext(request))

def items(request):
	if request.method == 'POST':
		all_items = Item.objects.filter(name__icontains = request.POST['search'])
		search = request.POST['search']
	else:
		all_items = Item.objects.all()
		search = ''
	return render_to_response('storage/items.html', 
		{'items': all_items, 'search':search}, 
		context_instance = RequestContext(request))

def categories(request):
	if request.method == 'POST':
		cats = Category.objects.filter(name__icontains = request.POST['search'])
		search = request.POST['search']
	else:
		cats = Category.objects.all()
		search = ''
	return render_to_response('storage/categories.html', 
		{'categories': cats, 'search': search}, 
		context_instance = RequestContext(request))

def storages(request):
	if request.method == 'POST':
		storages = Storage.objects.filter(name__icontains = request.POST['search'])
		search = request.POST['search']
	else:
		storages = Storage.objects.all()
		search = ''
	return render_to_response('storage/storages.html', 
		{'storages': storages, 'search': search}, 
		context_instance = RequestContext(request))

def clients(request):
	if request.method == 'POST':
		clients = Client.objects.filter( 
				Q(name__icontains = request.POST['search']) | 
				Q(address__icontains = request.POST['search']) )
		search = request.POST['search']
	else:
		clients = Client.objects.all()
		search = ''
	return render_to_response('storage/clients.html', 
		{'clients': clients, 'search': search}, 
		context_instance = RequestContext(request))

def clients_add(request):
	if request.method == 'POST':
		add_form = ClientAddForm(request.POST)
		if add_form.is_valid():
			new_cl = Client(name = add_form.cleaned_data['name'], address = add_form.cleaned_data['address'], zip_code = add_form.cleaned_data['zip_code'], country = add_form.cleaned_data['country'])
			new_cl.save()
			return HttpResponseRedirect('/clients/')
	else:
		add_form = ClientAddForm()
	return render_to_response('storage/clients_add.html', 
		{'form': add_form}, 
		context_instance = RequestContext(request))

def documents(request):
    return render_to_response('storage/documents.html', 
    	{}, 
    	context_instance = RequestContext(request))

def invoice(request):
	invoices = Document.objects.filter(doc_type__name__exact='invoice')
	return render_to_response('storage/invoice.html', 
		{'invoice_active':'active'}, 
		context_instance = RequestContext(request))

def invoice_add(request):
	if request.method == 'POST':
		pkeys = []
		net_prices = []
		for k,v in request.POST.iteritems():
			if k.startswith('item_id_'):
				try:
					pkey = int(v)
					pkeys.append(pkey)
				except:
					print 'incorrect item id: ' + v + ' for key ' + k
		items = ItemsBucket.objects.filter(pk__in = pkeys)
		for item in items:
			price = item.sell_price.amount
			tax = item.item.tax_rate.percentage
			net_prices.append(float(price - (price / 100) * tax))
		print net_prices
		client = Client.objects.get(pk = request.POST['client_id'])
		return render_to_response('storage/invoice_review.html', 
    		{'invoice_active':'active',
    		'invoice_number': request.POST['invoice_number'],
    		'client': client,
    		'items': items,
    		'net_prices': net_prices},
    		context_instance = RequestContext(request))
	else:
		clients = Client.objects.order_by('name')
		items = ItemsBucket.objects.all()
		return render_to_response('storage/invoice_add.html', 
    		{'invoice_active':'active', 
    		'clients': clients,
    		'items': items },
    		context_instance = RequestContext(request))

def mmplus(request):
    return render_to_response('storage/mmplus.html', 
    	{'mmplus_active':'active'}, 
    	context_instance = RequestContext(request))

def mmminus(request):
    return render_to_response('storage/mmminus.html', 
    	{'mmminus_active':'active'}, 
    	context_instance = RequestContext(request))

def pz(request):
    return render_to_response('storage/pz.html', 
    	{'pz_active':'active'}, 
    	context_instance = RequestContext(request))

def wz(request):
    return render_to_response('storage/wz.html', 
    	{'wz_active':'active'}, 
    	context_instance = RequestContext(request))

def reports(request):
    return render_to_response('storage/reports.html', 
    	{}, 
    	context_instance = RequestContext(request))