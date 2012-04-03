from django.template import RequestContext
from django.shortcuts import render_to_response
from models import Item, ItemsBucket, Category, Storage, Client

def index(request):
    return render_to_response('storage/index.html', {}, context_instance = RequestContext(request))

def items(request):
	if request.method == 'POST':
		all_items = Item.objects.filter(name__contains = request.POST['search'])
		search = request.POST['search']
	else:
		all_items = Item.objects.all()
		search = ''
	return render_to_response('storage/items.html', {'items': all_items, 'search':search}, context_instance = RequestContext(request))

def categories(request):
	if request.method == 'POST':
		pass
	else:
		pass
	cats = Category.objects.all()
	return render_to_response('storage/categories.html', {'categories': cats}, context_instance = RequestContext(request))

def storages(request):
	storages = Storage.objects.all()
	return render_to_response('storage/storages.html', {'storages': storages}, context_instance = RequestContext(request))

def clients(request):
	clients = Client.objects.all()
	return render_to_response('storage/clients.html', {'clients': clients}, context_instance = RequestContext(request))

def documents(request):
    return render_to_response('storage/documents.html', {}, context_instance = RequestContext(request))

def reports(request):
    return render_to_response('storage/reports.html', {}, context_instance = RequestContext(request))