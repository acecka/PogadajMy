from django.shortcuts import render
from django.views import View

from .models import Therapist, Client, Appointment, Link


class MakeAppointment(View):
    def get(self, request):
        therapists = Therapist.objects.all()
        clients = Client.objects.all()
        context = {
            'therapists': therapists,
            'clients': clients
        }
        return render(request, 'make_appointment.html', context)

    def post(self, request):
        therapist_id = request.POST.get('therapist')
        client_id = request.POST.get('client')
        date_and_time = request.POST.get('date_and_time')
        visit_length = request.POST.get('visit_length')

        therapist = Therapist.objects.get(id=therapist_id)
        client = Client.objects.get(id=client_id)

        appointment = Appointment.objects.create(
            therapist=therapist,
            client=client,
            date_and_time=date_and_time,
            visit_length=visit_length
        )

        appointment.save()

        return render(request, 'success.html')


class AboutUs(View):
    def get(self, request):
        therapists = Therapist.objects.all()
        context = {
            'therapists': therapists,
        }

        return render(request, 'about_us.html', context)


class Links(View):
    def get(self, request):
        links = Link.objects.all()
        return render(request, 'link_list.html', {'links': links})

class Contact(View):
    pass