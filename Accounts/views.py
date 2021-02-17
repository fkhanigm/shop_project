from django.shortcuts import render
from .forms import UserRegisterForm
from django.views.generic import DetailView, CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from Products import models as products_models

# Create your views here.


class SignUp(CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    success_message = 'your profile was created successfully'


class LogIn(LoginView):
    template_name = 'registration/login.html'


class LogOut(LogoutView):
    template_name = 'registration/logout.html'


class Profile(LoginRequiredMixin, DetailView):
    # loginRequiredMixin is for login required
    model = User
    template_name = 'profile/profile.html'
    # form_class = UserForm
    
    def get_object(self):
        #now we did not use pk for address the profile page of logined user and did not use pk for url
        return self.request.user
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category_list"] = products_models.Category.objects.all()
        return context

    # def form_valid(self, from):   # for check the form for edit profile
    #     form.save()
    #     retrun 


        