from django import forms

class InvoiceForm(forms.Form):
	invoice_number = forms.CharField(max_length = 100)
	client_id = forms.CharField(max_length = 10)
	form_of_payment = forms.CharField(max_length = 15)
	item_id_1 = forms.CharField(max_length = 10)
	item_amount_1 = forms.CharField(max_length = 10)

class InvoiceItem():
	ordinal = 0
	id = ""
	count = ""
	name = ""
	sell_price = ""
	tax = ""
	def __unicode__(self):
		return self.item_id + ' ' + self.item_count + ' ' + self.item_name + ' ' + self.item_sell_price + ' ' + self.item_tax