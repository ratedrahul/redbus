from django import forms
from buses.models import Bus

class BookingForm(forms.Form):
	bus_detail = forms.ChoiceField(label="Buses Available", widget=forms.Select)
	seat_number = forms.IntegerField()
	passenger_name = forms.CharField(max_length = 100)
	date = forms.DateField(widget=forms.SelectDateWidget())
	
	def __init__(self,*args,**kwargs):
		super(BookingForm,self).__init__(*args,**kwargs)
		self.fields['bus_detail'].choices = [((bus.id, bus.name)) for bus in Bus.objects.all()]

