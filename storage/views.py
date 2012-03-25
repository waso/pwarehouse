from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request):
    return render_to_response('storage/index.html', {},context_instance=RequestContext(request))

def items(request):
    return render_to_response('storage/items.html', {},context_instance=RequestContext(request))

def documents(request):
    return render_to_response('storage/documents.html', {},context_instance=RequestContext(request))

def reports(request):
    return render_to_response('storage/reports.html', {},context_instance=RequestContext(request))