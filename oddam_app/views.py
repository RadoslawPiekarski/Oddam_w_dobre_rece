from django.shortcuts import render
from django.views import View
from django.db.models import Sum
from .models import Donation

# Create your views here.


class LandingPage(View):
    def get(self, request):
        all_given_donations = list(Donation.objects.aggregate(Sum('quantity')).values())[0]
        print(all_given_donations)
        return render(request, "oddam_app/index.html", {
            "all_given_donations": all_given_donations,
        })


class AddDonation(View):
    def get(self, request):
        return render(request, "oddam_app/form.html")


class Login(View):
    def get(self, request):
        return render(request, "oddam_app/login.html")


class Register(View):
    def get(self, request):
        return render(request, "oddam_app/register.html")
