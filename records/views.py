from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from .models import Patient
from .models import Location

def home(request):
	context = {
		'patients': Patient.objects.all(),
		'title':'Home',
		'header':"Patient Records",
		'pageContent':"Here you can view all the patient records"
	}
	return render(request,'records/home.html',context)

class PatientViewLocations(TemplateView):
	template_name = "records/patientDetail.html"
	def get_context_data(self, **kwargs):
		patient = self.kwargs['patient']

		context = super().get_context_data(**kwargs)
		context['patient'] = Patient.objects.get(pk = patient)
		context['locationList'] = Location.objects.filter(Patient_id = patient)
		context['title'] = "Paitent Detail"
		context['header'] = "Paitent Detail"
		context['pageContent'] = "Here you can view all the details of patient record"
		return context