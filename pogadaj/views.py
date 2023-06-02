from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView

from .models import Therapist, Client, Appointment, AboutUs, Link, News, Contact
from templates.forms import LoginForm, RegisterForm, ResetPasswordForm


class MainPage(View):
    def get(self, request):
        links = Link.objects.all()
        about = AboutUs.objects.all()
        context = {
            'links': links,
            'about': about,
        }
        return render(request, 'main_page.html', context)


class MakeAppointment(View, LoginRequiredMixin):
    login_url = 'login/'

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


class OurTherapists(View):
    def get(self, request):
        therapists = Therapist.objects.all()
        context = {
            'therapists': therapists,
        }

        return render(request, 'our_therapists.html', context)


class ContactView(View):
    def get(self, request):
        contact = Contact.objects.all()
        context = {
            'contact': contact,
        }

        return render(request, 'contact.html', context)


class NewsView(View):
    def get(self, request):
        news = News.objects.all()
        context = {
            'news': news,
        }

        return render(request, 'news.html', context)


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', context={'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user.is_authenticated:
                login(request, user)
            else:
                form.add_error(None, 'Invalid username or password')

        return render(request, 'login.html', context={'form': form})


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        if User.objects.filter(username=form.cleaned_data['username']).exists():
            form.add_error('username already exists')
            return super().form_valid(form)
        if form.cleaned_data['password'] != form.cleaned_data['repeat_password']:
            form.add_error('passwords do not match')
            return super().form_valid(form)

        User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password'],
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
            email=form.cleaned_data['email'],
        )

        return super().form_valid(form)


class ResetPasswordView(View):
    def get(self, request, id):
        form = ResetPasswordForm()
        return render(request, 'reset_password.html', {'form': form})

    def post(self, request, id):
        form = ResetPasswordForm(request.POST)

        if form.is_valid():
            user = User.objects.get(id=int(id))
            new_password = form.cleaned_data['new_password']
            repeat_password = form.cleaned_data['repeat_password']

            if new_password != repeat_password:
                form.add_error('repeat_password', 'Passwords do not match')
                return render(request, 'reset_password.html', {'form': form})

            user.set_password(new_password)
            user.save()
            return redirect('success')

        return render(request, 'reset_password.html', {'form': form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('index')

